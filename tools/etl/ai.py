"""
Module: ai.py
Purpose: Leverages Google Gemini via Structured Outputs (Pydantic) to evaluate, filter, 
and strictly classify scraped articles into ISTQB domains. Implements rate limiting.
"""
import os
import json
import time
import logging
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
        description="True ONLY if the article is relevant for a QA Engineer (Testing theory, QA automation, networks, databases, API). False if it is pure software development (RxJava, Android Studio) or irrelevant hardware/OS."
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

class BatchDecision(BaseModel):
    decisions: list[ArticleDecision]

def classify_articles(articles: list, chunk_size: int = 30) -> list:
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
        # We only send necessary fields to save tokens
        prompt_data = [{"id": a['id'], "title": a['title'], "url": a['url']} for a in chunk]
        
        prompt = (
            "You are an expert QA Manager strictly adhering to the ISTQB syllabus.\n"
            "Evaluate the following articles. Discard irrelevant ones (keep: False). "
            "For relevant ones, assign the single most accurate ISTQB domain category.\n\n"
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
            res_dict = json.loads(response.text)
            decision_map = {d['id']: d for d in res_dict['decisions']}
            
            # Map AI decisions back to our article objects
            for a in chunk:
                decision = decision_map.get(a['id'])
                if decision and decision.get('keep'):
                    a['keep'] = True
                    a['category'] = decision.get('category')
                    logger.debug(f"[KEEP -> {a['category']}] {a['title'][:40]}")
                else:
                    a['keep'] = False
                    logger.debug(f"[DISCARD] {a['title'][:40]}")
                classified.append(a)
                
        except Exception as e:
            logger.error(f"Batch classification failed. Marking chunk as discarded. Error: {e}")
            # Failsafe: if the API request fails, mark all articles in this chunk as False to prevent bad data
            for a in chunk:
                a['keep'] = False
                classified.append(a)
                
    return classified
