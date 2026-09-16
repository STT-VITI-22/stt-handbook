import logging
import asyncio
from bs4 import BeautifulSoup
from .base import BaseParser
import urllib.parse

logger = logging.getLogger(__name__)

class HabrParser(BaseParser):
    def __init__(self, output_dir: str, target_urls: list = None):
        super().__init__(output_dir)
        self.target_urls = target_urls or []

    async def run(self):
        for url in self.target_urls:
            logger.info(f"Habr: Parsing {url}")
            await self._parse_article(url)

    async def _parse_article(self, url: str):
        soup = await self.fetch_html(url)
        if not soup:
            return
        
        # Target specific container for Habr
        article_body = soup.find("div", class_="article-formatted-body")
        if not article_body:
            logger.error(f"Could not find main content on Habr for {url}")
            return
            
        # Clean unwanted tags
        for unwanted in article_body.find_all(['nav', 'script', 'style', 'iframe']):
            unwanted.decompose()

        title_elem = soup.find("h1")
        title = title_elem.get_text(strip=True) if title_elem else "habr_article"
        
        clean_title = self.get_safe_filename(title, url)
        md_content = self.html_to_markdown(article_body)
        
        # Write to file
        file_path = f"{self.output_dir}/{clean_title}.md"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"# {title}\n\n{md_content}")
        logger.info(f"Saved: {file_path}")
