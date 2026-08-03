"""
Module: ai.py
Purpose: Leverages Google Gemini via Structured Outputs (Pydantic) to evaluate, filter, 
and strictly classify scraped articles into ISTQB domains. Implements rate limiting.
"""
import os
import json
import time
import logging
import asyncio
import httpx
from bs4 import BeautifulSoup
from typing import Literal
from pydantic import BaseModel, Field
from google import genai
from google.genai import types

logger = logging.getLogger(__name__)

# Strict Enum representing the target classification domains based on ISTQB syllabus.
# The AI is forced by Pydantic to choose ONLY from these exact strings if keep is True.
ISTQBDomain = Literal[
    "sdlc", "test_levels", "test_types", "maintenance_testing",
    "static_testing", "test_design_techniques", "test_management",
    "defect_management", "tool_support", "api_testing",
    "performance_testing", "security_testing", "networks_databases"
]

class ArticleDecision(BaseModel):
    id: int
    keep: bool = Field(
        description="True ONLY if the article is relevant for a QA Engineer (Testing theory, QA automation, networks, databases, API) OR if it is a training course that contains a syllabus or curriculum. False if it is pure software development (RxJava, Android Studio), irrelevant hardware/OS, or pure marketing with no syllabus."
    )
    category: ISTQBDomain | None = Field(
        description="""If keep is True, strictly classify the article into one of these ISTQB domains:
- sdlc: Software Development Lifecycle, Agile, Scrum methodologies.
- test_levels: Component, Integration, System, and Acceptance testing.
- test_types: Functional, Non-functional, White-box, Black-box testing.
- maintenance_testing: Testing software changes, impact analysis.
- static_testing: Code reviews, static analysis tools, inspection.
- test_design_techniques: Equivalence partitioning, boundary value analysis, decision tables.
- test_management: Test planning, estimation, monitoring, risk management.
- defect_management: Bug tracking, defect life cycle.
- tool_support: Testing tools, CI/CD, automation frameworks (Selenium, Cypress).
- api_testing: REST, SOAP, HTTP methods, Postman.
- performance_testing: Load, stress, volume, scalability testing.
- security_testing: Vulnerabilities, OWASP, penetration testing.
- networks_databases: OSI model, TCP/IP, SQL, basic DB architecture.
Return null if keep is False."""
    )

async def fetch_snippet(client, url):
    """
    Fetches the first 500 characters of the main content from a given URL.
    This provides the AI with actual textual context (a 'snippet') rather than relying purely on the title, 
    significantly improving categorization accuracy and preventing hallucination.
    
    Args:
        client (httpx.AsyncClient): The async HTTP client.
        url (str): The target article URL.
        
    Returns:
        str: A truncated string of the article's text content.
    """
    try:
        resp = await client.get(url, timeout=5.0)
        soup = BeautifulSoup(resp.content, 'html.parser')
        content = soup.select_one('div.single-knowledge-base-content') or soup.body
        text = content.get_text(separator=' ', strip=True) if content else ""
        return text[:500]
    except Exception:
        return ""

async def fetch_all_snippets(chunk):
    """
    Asynchronously fetches content snippets for a batch (chunk) of articles concurrently.
    This optimizes network I/O during the classification phase without causing major bottlenecks.
    
    Args:
        chunk (list): A list of article dictionaries containing 'url' keys.
        
    Returns:
        list: A list of text snippets corresponding to the articles in the chunk.
    """
    async with httpx.AsyncClient() as client:
        tasks = [fetch_snippet(client, a['url']) for a in chunk]
        return await asyncio.gather(*tasks)

class BatchDecision(BaseModel):
    decisions: list[ArticleDecision]

async def classify_articles(articles: list, chunk_size: int = 30) -> list:
    """
    Evaluates a list of articles using Gemini. Implements a sliding window rate limiter
    to comply with free tier API limits (5 Requests Per Minute).
    
    Args:
        articles (list): List of article dictionaries.
        chunk_size (int): Number of articles to send per API request.
        
    Returns:
        list: The same list of articles, enriched with 'keep' and 'category' flags.
    """
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        logger.error("GEMINI_API_KEY not found in environment. Aborting classification.")
        return articles

    client = genai.Client()
    classified = []
    
    # Assign temporary sequential IDs for reliable mapping from the AI response
    for i, a in enumerate(articles):
        a['id'] = i
        
    request_times = []
    
    # Process articles in batches
    for i in range(0, len(articles), chunk_size):
        # --- Sliding Window Rate Limiting Logic ---
        current_time = time.time()
        # Keep only request timestamps from the last 60 seconds
        request_times = [t for t in request_times if current_time - t < 60]
        
        # If we've made 4 requests in the last minute, pause before making the 5th
        if len(request_times) >= 4:
            sleep_time = 60 - (current_time - request_times[0])
            if sleep_time > 0:
                logger.info(f"API Rate Limit Protection: Sleeping for {sleep_time:.1f}s...")
                time.sleep(sleep_time)
                
        request_times.append(time.time())
        # ------------------------------------------
        
        chunk = articles[i:i+chunk_size]
        
        logger.info(f"Fetching content snippets for {len(chunk)} articles to improve AI accuracy...")
        try:
            snippets = await fetch_all_snippets(chunk)
        except Exception as e:
            logger.warning(f"Snippet fetching failed: {e}")
            snippets = ["" for _ in chunk]
            
        # We only send necessary fields to save tokens
        prompt_data = [{"id": a['id'], "title": a['title'], "url": a['url'], "content_snippet": snippets[idx]} for idx, a in enumerate(chunk)]
        
        prompt = (
            "You are an expert QA Manager strictly adhering to the ISTQB syllabus.\n"
            "Evaluate the following articles using their titles, URLs, and text snippets. Discard irrelevant ones (keep: False). "
            "For relevant ones, assign the single most accurate ISTQB domain category based on the actual content.\n\n"
            f"{json.dumps(prompt_data, ensure_ascii=False)}"
        )
        
        logger.info(f"Sending batch {i//chunk_size + 1}/{(len(articles)-1)//chunk_size + 1} ({len(chunk)} articles)...")
        
        try:
            response = client.models.generate_content(
                model='gemini-3.6-flash',
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=BatchDecision,
                    temperature=0.0 # Deterministic classification to prevent hallucination
                ),
            )
            res_data = BatchDecision.model_validate_json(response.text)
            decision_map = {d.id: d for d in res_data.decisions}
            
            # Map AI decisions back to our article objects
            for article in chunk:
                decision = decision_map.get(article['id'])
                if decision:
                    article['keep'] = decision.keep
                    
                    # HARD OVERRIDE: We bypass AI classification for training courses.
                    # Any URL containing '/kursy/' is guaranteed to be physically placed in the 'courses' directory.
                    # This completely eliminates the risk of AI misclassifying informative articles (like dictionaries) as courses.
                    if article['keep'] and '/kursy/' in article['url']:
                        article['category'] = 'courses'
                    else:
                        article['category'] = decision.category
                else:
                    article['keep'] = False
                
                classified.append(article)
                logger.info(f"Classified '{article['title']}': keep={article.get('keep')}, category={article.get('category')}")
                
        except Exception as e:
            logger.error(f"Batch classification failed. Marking chunk as discarded. Error: {e}")
            # Failsafe: if the API request fails, mark all articles in this chunk as False to prevent bad data
            for a in chunk:
                a['keep'] = False
                classified.append(a)
                
    return classified
