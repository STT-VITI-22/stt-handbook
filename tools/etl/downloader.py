"""
Module: downloader.py
Purpose: Downloads the raw HTML of approved articles and extracts the main content 
into clean Markdown. It uses explicit CSS selectors (if provided in config) for 100% 
accuracy, or falls back to 'trafilatura' for universal heuristic extraction.
"""
import os
import asyncio
import httpx
import trafilatura
from bs4 import BeautifulSoup
import markdownify
from slugify import slugify
import logging

logger = logging.getLogger(__name__)

def get_safe_filename(title: str, url: str) -> str:
    safe = slugify(title)
    if not safe and url:
        safe = slugify(url.split('/')[-2]) if url.endswith('/') else slugify(url.split('/')[-1])
    return safe or f"article-{hash(url) % 10000}"

async def download_article(client: httpx.AsyncClient, item: dict, base_dir: str, strategy: str, sources_config: list):
    if not item.get("keep"):
        return
        
    url = item['url']
    source_name = item.get('source_name') or 'unknown_source'
    
    # ---------------------------------------------------------
    # ROUTING LOGIC: Determine the target output folder
    # ---------------------------------------------------------
    category = item.get('category')
    if category == 'courses':
        # HARD OVERRIDE: Educational courses must always be physically isolated in the 'courses' folder.
        # This takes precedence even if the user selected the 'source' (original menu) strategy.
        folder_name = 'courses'
    elif strategy == 'topic':
        # 'topic' strategy uses the strict ISTQB domain provided by the AI classification
        folder_name = category or 'uncategorized'
    else:
        # 'source' strategy preserves the original hierarchical folder structure from the website
        folder_name = source_name
        
    target_dir = os.path.join(base_dir, folder_name)
    os.makedirs(target_dir, exist_ok=True)
    
    # Find the specific config for this source to get the content_selector
    # Because source_name can contain subdirectories (e.g., 'qalight_baza/osnovi'), we use startswith
    source_cfg = next((s for s in sources_config if source_name.startswith(s['name'])), {})
    content_selector = source_cfg.get('content_selector')
    exclude_selectors = source_cfg.get('exclude_selectors', [])
    
    try:
        resp = await client.get(url, follow_redirects=True)
        resp.raise_for_status()
        
        markdown_text = None
        html_content = resp.text
        
        # 1. Try Exact CSS Selector Extraction (Most Reliable)
        if content_selector:
            soup = BeautifulSoup(html_content, 'lxml')
            content_block = soup.select_one(content_selector)
            if content_block:
                # Clean up junk elements like scripts and ads within the block
                for tag in content_block(["script", "style", "nav", "footer", "iframe"]):
                    tag.decompose()
                    
                # Clean up specific elements passed from config (like embedded menus/sidebars)
                for sel in exclude_selectors:
                    for tag in content_block.select(sel):
                        tag.decompose()
                        
                import re
                # ---------------------------------------------------------
                # CONTENT SANITIZATION & MARKDOWN CONVERSION
                # ---------------------------------------------------------
                # 1. Escape literal HTML tags (e.g., <html>) found in the text.
                # Standard markdown parsers treat raw HTML tags as invisible structural elements.
                # By wrapping them in backticks (`<html>`), they are safely rendered as inline code blocks.
                for text_node in content_block.find_all(string=True):
                    if '<' in text_node and '>' in text_node:
                        new_text = re.sub(r'(<[^>]+>)', r'`\1`', text_node)
                        text_node.replace_with(new_text)
                        
                # 2. Convert the sanitized HTML to Markdown format.
                # The 'keep_inline_images_in' parameter prevents markdownify from destroying <img> tags 
                # that are nested inside headers (h1-h6), paragraphs, or links.
                markdown_text = markdownify.markdownify(
                    str(content_block), 
                    heading_style="ATX",
                    keep_inline_images_in=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'div', 'a', 'td', 'th', 'span', 'strong', 'em', 'b', 'i']
                ).strip()
            else:
                logger.warning(f"Selector '{content_selector}' not found on {url}. Falling back to Trafilatura.")
        
        # 2. Fallback to Heuristic Extraction (Trafilatura)
        if not markdown_text:
            markdown_text = trafilatura.extract(html_content, output_format="markdown", include_links=True)
            
        if not markdown_text:
            logger.error(f"Failed to extract ANY content for {url}. Skipping.")
            return
            
        safe_filename = get_safe_filename(item['title'], url)
        filepath = os.path.join(target_dir, f"{safe_filename}.md")
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# {item['title']}\n\n**Source:** {url}\n\n---\n\n{markdown_text}")
            
    except Exception as e:
        logger.error(f"Failed to download {url}: {e}")

async def download_all(articles: list, base_dir: str, strategy: str, sources_config: list):
    logger.info(f"Starting parallel download for {len(articles)} approved articles. Strategy: {strategy}")
    
    limits = httpx.Limits(max_connections=5)
    async with httpx.AsyncClient(timeout=20.0, limits=limits) as client:
        tasks = [download_article(client, a, base_dir, strategy, sources_config) for a in articles]
        await asyncio.gather(*tasks)
