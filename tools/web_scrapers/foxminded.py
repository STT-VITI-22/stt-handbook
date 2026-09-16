import logging
import asyncio
from bs4 import BeautifulSoup
from .base import BaseParser
import urllib.parse

logger = logging.getLogger(__name__)

class FoxmindedParser(BaseParser):
    def __init__(self, output_dir: str, target_urls: list = None):
        super().__init__(output_dir)
        self.target_urls = target_urls or []

    async def run(self):
        for url in self.target_urls:
            logger.info(f"Foxminded: Parsing {url}")
            await self._parse_article(url)

    async def _parse_article(self, url: str):
        soup = await self.fetch_html(url)
        if not soup:
            return
        
        # Target specific container
        article_body = soup.find("div", class_="article article-post")
        if not article_body:
            # Fallback to general content area if article class changes
            article_body = soup.find("div", class_="content")
            
        if not article_body:
            logger.error(f"Could not find main content on Foxminded for {url}")
            return
            
        # Remove noisy elements
        for unwanted in article_body.find_all(['nav', 'script', 'style', 'iframe']):
            unwanted.decompose()
            
        # Try to remove "Similar materials" block at the bottom
        for h2 in article_body.find_all("h2"):
            if "Схожі матеріали" in h2.get_text():
                # Decompose everything after this header
                for sib in h2.find_next_siblings():
                    sib.decompose()
                h2.decompose()
                break

        title_elem = soup.find("h1")
        title = title_elem.get_text(strip=True) if title_elem else "foxminded_article"
        
        clean_title = self.get_safe_filename(title, url)

        md_content = self.html_to_markdown(article_body)
        
        # Write to file
        file_path = f"{self.output_dir}/{clean_title}.md"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"# {title}\n\n{md_content}")
        logger.info(f"Saved: {file_path}")
