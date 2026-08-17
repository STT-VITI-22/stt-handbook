import asyncio
import logging
from bs4 import BeautifulSoup
from .base import BaseParser

logger = logging.getLogger(__name__)

class QalightParser(BaseParser):
    def __init__(self, output_dir: str = "dataset/qalight/parsed"):
        super().__init__(output_dir=output_dir)
        self.base_url = "https://qalight.ua/baza-znan/"

    def _find_parent_category(self, element) -> str:
        """
        Walks up the DOM tree from the article link to find its parent category in the menu.
        """
        parent = element.find_parent("li", class_="menu-item-has-children")
        if parent:
            name_tag = parent.find("> a") or parent.find("a")
            if name_tag:
                return name_tag.get_text(strip=True)
        return "uncategorized"

    def _clean_slug(self, text: str) -> str:
        # Simplifies category names for folder usage (e.g. "Типи тестування" -> "tipi-testuvannia")
        from slugify import slugify
        return slugify(text)

    async def _process_article(self, url: str, category: str, title: str):
        soup = await self.fetch_html(url)
        if not soup:
            return

        content_block = soup.select_one("div.single-knowledge-base-content")
        if not content_block:
            logger.warning(f"Could not find main content on {url}. Skipping.")
            return

        # Clean junk
        for tag in content_block(["script", "style", "nav", "footer", "iframe"]):
            tag.decompose()
        for sel in [".carousel-block", "ul.sub-menu", "ul.menu", ".sidebar", ".widget"]:
            for tag in content_block.select(sel):
                tag.decompose()

        # Convert to markdown using the base class robust method
        md = self.html_to_markdown(content_block)
        if md:
            await self.save_article(url, category, title, md)

    async def run(self):
        logger.info(f"Starting parsing for QALight Base URL: {self.base_url}")
        soup = await self.fetch_html(self.base_url)
        if not soup:
            return

        links = soup.select("ul.innermenu li ul.sub-menu li ul.sub-menu li a")
        logger.info(f"Discovered {len(links)} articles.")

        tasks = []
        for a_tag in links:
            url = a_tag.get('href')
            title = a_tag.get_text(strip=True)
            
            # Hard override for courses
            if '/kursy/' in url:
                category = "courses"
            else:
                raw_cat = self._find_parent_category(a_tag)
                category = self._clean_slug(raw_cat)
            
            tasks.append(self._process_article(url, category, title))

        # Run concurrently with a slight limit to avoid destroying the target server
        logger.info("Downloading articles concurrently...")
        await asyncio.gather(*tasks)
        logger.info("QALight parsing complete.")
