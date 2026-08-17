import asyncio
import logging
from bs4 import BeautifulSoup
from .base import BaseParser

logger = logging.getLogger(__name__)

class DouParser(BaseParser):
    def __init__(self, output_dir: str = "dataset/dou/parsed"):
        # We will save all provided DOU articles directly into one category folder for now
        super().__init__(output_dir=output_dir)
        
        # Hardcoded targets provided by the user
        self.target_urls = [
            "https://dou.ua/forums/topic/44882/",
            "https://dou.ua/forums/topic/13389/",
            "https://dou.ua/forums/topic/14015/"
        ]

    async def _process_article(self, url: str):
        soup = await self.fetch_html(url)
        if not soup:
            return

        # 1. Extract title from <h1>
        h1_tag = soup.find('h1')
        title = h1_tag.get_text(strip=True) if h1_tag else "dou_article"

        # 2. Extract content block
        content_block = soup.select_one('article.b-typo')
        if not content_block:
            logger.warning(f"Could not find main content (article.b-typo) on {url}. Skipping.")
            return

        # Clean junk (like scripts, social buttons, etc.)
        for tag in content_block(["script", "style", "nav", "footer", "iframe"]):
            tag.decompose()
            
        # DOU specific cleanup (author block, share block, etc. inside the article if any)
        for sel in [".author-info", ".share-block", ".wrap_comments"]:
            for tag in content_block.select(sel):
                tag.decompose()

        # Convert to markdown using the base class robust method
        md = self.html_to_markdown(content_block)
        if md:
            # We pass empty string for category because the output_dir already includes '/articles'
            await self.save_article(url, category="", title=title, markdown_text=md)

    async def run(self):
        logger.info(f"Starting parsing for {len(self.target_urls)} specific DOU URLs")

        tasks = []
        for url in self.target_urls:
            tasks.append(self._process_article(url))

        # Run concurrently
        logger.info("Downloading articles concurrently...")
        await asyncio.gather(*tasks)
        logger.info("DOU parsing complete.")
