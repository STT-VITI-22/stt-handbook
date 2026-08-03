"""
Module: discovery.py
Purpose: Handles the asynchronous scraping of target URLs to extract article links 
based on configurable CSS selectors defined in sources.yaml.
"""
import httpx
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from slugify import slugify
import logging

logger = logging.getLogger(__name__)

async def discover_links(sources_config: list) -> list:
    """
    Scrapes the provided source URLs and extracts links using CSS selectors.
    
    Args:
        sources_config (list): A list of dictionaries containing 'url', 'link_selector', and 'name'.
        
    Returns:
        list: A list of discovered article metadata dictionaries.
    """
    discovered = []
    seen_urls = set()
    
    # Using httpx for non-blocking asynchronous HTTP requests
    async with httpx.AsyncClient(timeout=15.0) as client:
        for source in sources_config:
            url = source.get('url')
            selector = source.get('link_selector')
            source_name = source.get('name')
            category_container = source.get('category_container')
            category_name_tag = source.get('category_name_tag')
            
            logger.info(f"Scanning source: {source_name} ({url})")
            try:
                # Follow redirects to ensure we land on the correct page
                resp = await client.get(url, follow_redirects=True)
                resp.raise_for_status() 
                
                soup = BeautifulSoup(resp.text, 'lxml')
                
                # Select all anchor tags that match the config's CSS selector
                links = soup.select(selector)
                for link in links:
                    href = link.get('href')
                    # Ignore empty links or anchor-only links
                    if not href or href == '#':
                        continue
                    
                    # Convert relative paths to absolute URLs based on the source URL
                    full_url = urljoin(url, href)
                    
                    # Prevent duplicate processing of the same URL
                    if full_url in seen_urls:
                        continue
                    seen_urls.add(full_url)
                    
                    # Attempt to extract category name from parent elements (if configured)
                    # This recreates the original 'by-source' directory hierarchy universally
                    final_source_name = source_name
                    if category_container and category_name_tag:
                        tag_name = category_container.split('.')[0]
                        class_name = category_container.split('.')[1] if '.' in category_container else None
                        
                        parent_node = link.find_parent(tag_name, class_=class_name)
                        if parent_node:
                            cat_tag = parent_node.find(category_name_tag)
                            if cat_tag:
                                safe_cat = slugify(cat_tag.get_text(strip=True))
                                final_source_name = f"{source_name}/{safe_cat}"
                    
                    discovered.append({
                        "url": full_url,
                        "title": link.get_text(strip=True),
                        "source_name": final_source_name
                    })
            except Exception as e:
                logger.error(f"Failed to scan {url}. Reason: {e}")
                
    return discovered
