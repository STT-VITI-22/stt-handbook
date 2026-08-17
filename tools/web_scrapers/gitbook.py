import os
import re
import asyncio
import httpx
from bs4 import BeautifulSoup
import logging
from slugify import slugify

logger = logging.getLogger(__name__)

class GitBookParser:
    """
    Парсер для сайтів на базі GitBook, який використовує стандарт llms.txt
    та вбудовану генерацію Markdown (.md) від самого GitBook.
    """
    def __init__(self, base_url: str, output_dir: str):
        self.base_url = base_url.rstrip("/")
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        self.client = httpx.AsyncClient(timeout=30.0, follow_redirects=True, limits=httpx.Limits(max_connections=5))

    def get_safe_filename(self, title: str, url: str) -> str:
        safe = slugify(title)
        if not safe:
            parts = [p for p in url.split('/') if p and not p.endswith('.md')]
            safe = slugify(parts[-1]) if parts else f"article-{hash(url) % 10000}"
        return safe

    async def fetch_llms_txt(self) -> list[str]:
        """Завантажує llms.txt та витягує всі посилання на сторінки у форматі .md."""
        url = f"{self.base_url}/llms.txt"
        logger.info(f"Завантаження списку сторінок: {url}")
        try:
            resp = await self.client.get(url)
            resp.raise_for_status()
            text = resp.text
            # Шукаємо всі посилання, що закінчуються на .md
            links = re.findall(r'\[.*?\]\((https?://[^)]+\.md)\)', text)
            return list(set(links))
        except Exception as e:
            logger.error(f"Не вдалося завантажити llms.txt: {e}")
            return []

    async def fetch_and_save_page(self, md_url: str):
        """Завантажує готовий Markdown сторінки, фіксить шляхи до картинок та зберігає."""
        try:
            resp = await self.client.get(md_url)
            resp.raise_for_status()
            md_text = resp.text

            # Відкидаємо шапку (GitBook додає абзац про llms.txt зверху кожної .md сторінки)
            # Приклад: "> For the complete documentation index, see [llms.txt]..."
            md_text = re.sub(r'^> For the complete documentation index, see \[llms\.txt\].*?\n+', '', md_text, flags=re.MULTILINE)

            # Витягуємо H1 для назви файлу
            title_match = re.search(r'^#\s+(.+)$', md_text, flags=re.MULTILINE)
            title = title_match.group(1).strip() if title_match else "Без назви"

            # Фіксимо посилання на зображення (відносні на абсолютні)
            # В GitBook вони часто виглядають як <img src="/files/...">
            base_domain = "/".join(self.base_url.split("/")[:3]) # e.g. https://vladislaveremeev.gitbook.io
            md_text = md_text.replace('src="/files/', f'src="{base_domain}/files/')
            md_text = md_text.replace('href="/files/', f'href="{base_domain}/files/')
            md_text = md_text.replace('](/files/', f']({base_domain}/files/')

            # Визначаємо категорію на основі URL (якщо це не корінь)
            path_parts = md_url.replace(self.base_url, "").strip("/").split("/")
            if len(path_parts) > 1:
                category = slugify(path_parts[0])
            else:
                category = "z_general"

            target_dir = os.path.join(self.output_dir, category)
            os.makedirs(target_dir, exist_ok=True)
            
            safe_filename = self.get_safe_filename(title, md_url)
            filepath = os.path.join(target_dir, f"{safe_filename}.md")
            
            with open(filepath, 'w', encoding='utf-8') as f:
                source_url = md_url.replace(".md", "")
                f.write(f"# {title}\n\n**Source:** {source_url}\n\n---\n\n{md_text}")
            
            logger.info(f"Збережено: {filepath}")

        except Exception as e:
            logger.error(f"Помилка при обробці {md_url}: {e}")

    async def run(self):
        links = await self.fetch_llms_txt()
        logger.info(f"Знайдено сторінок: {len(links)}")
        
        # Обробляємо паралельно батчами
        batch_size = 10
        for i in range(0, len(links), batch_size):
            batch = links[i:i+batch_size]
            tasks = [self.fetch_and_save_page(url) for url in batch]
            await asyncio.gather(*tasks)

    async def close(self):
        await self.client.aclose()
