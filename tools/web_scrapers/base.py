import os
import re
import asyncio
import httpx
from bs4 import BeautifulSoup
import markdownify
from slugify import slugify
import logging

logger = logging.getLogger(__name__)

class BaseParser:
    """
    Abstract base parser that provides common utilities for fetching pages 
    and converting HTML to robust Markdown. Each source should subclass this.
    """
    def __init__(self, output_dir: str):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        self.client = httpx.AsyncClient(timeout=20.0, follow_redirects=True, limits=httpx.Limits(max_connections=5))

    async def fetch_html(self, url: str) -> BeautifulSoup | None:
        try:
            resp = await self.client.get(url)
            resp.raise_for_status()
            return BeautifulSoup(resp.text, 'lxml')
        except Exception as e:
            logger.error(f"Failed to fetch {url}: {e}")
            return None

    def get_safe_filename(self, title: str, url: str) -> str:
        safe = slugify(title)
        if not safe and url:
            safe = slugify(url.split('/')[-2]) if url.endswith('/') else slugify(url.split('/')[-1])
        return safe or f"article-{hash(url) % 10000}"

    def html_to_markdown(self, content_block: BeautifulSoup) -> str:
        """
        Converts a BeautifulSoup tag into robust Markdown.
        Escapes raw HTML tags and preserves inline images.
        """
        for text_node in content_block.find_all(string=True):
            if '<' in text_node and '>' in text_node:
                new_text = re.sub(r'(<[^>]+>)', r'`\1`', text_node)
                text_node.replace_with(new_text)

        md = markdownify.markdownify(
            str(content_block), 
            heading_style="ATX",
            keep_inline_images_in=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'div', 'a', 'td', 'th', 'span', 'strong', 'em', 'b', 'i']
        ).strip()
        return md

    async def save_article(self, url: str, category: str, title: str, markdown_text: str):
        """
        Saves the markdown text to the correct category folder within output_dir.
        """
        target_dir = os.path.join(self.output_dir, category)
        os.makedirs(target_dir, exist_ok=True)
        
        safe_filename = self.get_safe_filename(title, url)
        filepath = os.path.join(target_dir, f"{safe_filename}.md")
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# {title}\n\n**Source:** {url}\n\n---\n\n{markdown_text}")
        
        logger.info(f"Saved: {filepath}")

    async def run(self):
        """
        Main execution logic to be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses must implement the run() method.")

    async def close(self):
        await self.client.aclose()
