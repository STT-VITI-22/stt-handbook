import os
import asyncio
import httpx
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from urllib.parse import urljoin, urlparse
from deep_translator import GoogleTranslator
from slugify import slugify

BASE_URL = "https://qalight.ua/baza-znan/"
DOMAIN = "https://qalight.ua"
DATASET_DIR = "../qalight"

# Ініціалізуємо перекладач (з української на англійську)
translator = GoogleTranslator(source='uk', target='en')

def get_intelligent_name(ukr_text):
    """
    Перекладає текст англійською та робить з нього безпечний slug 
    (наприклад: "Базовий модуль тестування" -> "basic-testing-module")
    """
    try:
        translated = translator.translate(ukr_text)
        return slugify(translated)
    except Exception as e:
        print(f"Помилка перекладу '{ukr_text}': {e}")
        return slugify(ukr_text)

async def download_image(client, img_url, save_path):
    try:
        response = await client.get(img_url, follow_redirects=True)
        response.raise_for_status()
        with open(save_path, 'wb') as f:
            f.write(response.content)
        return True
    except Exception as e:
        return False

async def process_article(client, url, category_path):
    print(f"  Стаття: {url}")
    try:
        response = await client.get(url, follow_redirects=True)
        soup = BeautifulSoup(response.text, 'lxml')
        
        # Заголовок (зберігаємо оригінал для тексту, перекладаємо для файлу)
        title_tag = soup.find('h1')
        if title_tag:
            title_ukr = title_tag.get_text(strip=True)
        else:
            title_ukr = soup.title.string.split('-')[0].strip() if soup.title else "Без назви"
        safe_filename = get_intelligent_name(title_ukr)
        
        # ЕКСТРАКЦІЯ КОНТЕНТУ (Уніфікована і точна)
        # На сайті QALight весь корисний текст статті лежить у конкретному блоці:
        content_container = soup.find('div', class_='single-knowledge-base-content')
        
        # Якщо з якоїсь причини цього блоку немає, беремо резервний варіант, але відкидаємо сайдбари
        if not content_container:
            content_container = soup.find('article') or soup.find('main')
            # Відкидаємо меню та футери, якщо довелося брати широку область
            if content_container:
                for unwanted in content_container.find_all(['nav', 'footer', 'aside', 'header']):
                    unwanted.decompose()
        
        if not content_container:
            print(f"    Не знайдено контенту для {url}")
            return

        # Видаляємо технічне сміття (скрипти, стилі)
        for unwanted in content_container.find_all(['script', 'style', 'noscript', 'meta', 'link', 'iframe']):
            unwanted.decompose()

        assets_dir = os.path.join(category_path, "assets")
        os.makedirs(assets_dir, exist_ok=True)

        for img in content_container.find_all('img'):
            src = img.get('src')
            if not src: continue
            
            img_url = urljoin(url, src)
            img_name = os.path.basename(urlparse(img_url).path)
            if not img_name:
                img_name = "image.jpg"
                
            local_img_path = os.path.join(assets_dir, img_name)
            
            if await download_image(client, img_url, local_img_path):
                img['src'] = f"assets/{img_name}"

        # Конвертуємо у Markdown. heading_style="ATX" дає класичні # Заголовки
        markdown_text = md(str(content_container), heading_style="ATX")
        
        md_file_path = os.path.join(category_path, f"{safe_filename}.md")
        with open(md_file_path, 'w', encoding='utf-8') as f:
            # В шапці зберігаємо оригінальну назву і лінк для бекапу
            f.write(f"# {title_ukr}\n")
            f.write(f"**Translated Slug:** {safe_filename}\n")
            f.write(f"**Source:** [{url}]({url})\n\n---\n\n")
            f.write(markdown_text)
            
        print(f"    -> Збережено: {md_file_path}")

    except Exception as e:
        print(f"    Помилка при обробці {url}: {e}")

async def main():
    os.makedirs(DATASET_DIR, exist_ok=True)
    
    async with httpx.AsyncClient(timeout=30.0) as client:
        print("Читання головної сторінки...")
        response = await client.get(BASE_URL, follow_redirects=True)
        soup = BeautifulSoup(response.text, 'lxml')
        
        menu = soup.find('ul', class_='innermenu')
        if not menu: return
            
        for category_li in menu.find_all('li', recursive=False):
            category_a = category_li.find('a')
            if not category_a: continue
            
            ukr_cat = category_a.get_text(strip=True)
            cat_name = get_intelligent_name(ukr_cat)
            
            sub_menu = category_li.find('ul', class_='sub-menu')
            if sub_menu:
                for sub_category_li in sub_menu.find_all('li', recursive=False):
                    sub_category_a = sub_category_li.find('a')
                    if not sub_category_a: continue
                    
                    ukr_subcat = sub_category_a.get_text(strip=True)
                    subcat_name = get_intelligent_name(ukr_subcat)
                    
                    category_path = os.path.join(DATASET_DIR, cat_name, subcat_name)
                    os.makedirs(category_path, exist_ok=True)
                    print(f"\n[Папка] {ukr_cat} -> {ukr_subcat} | Збережено як: {cat_name}/{subcat_name}")
                    
                    articles_menu = sub_category_li.find('ul', class_='sub-menu')
                    if articles_menu:
                        for article_li in articles_menu.find_all('li', recursive=False):
                            article_a = article_li.find('a')
                            if not article_a: continue
                            article_url = article_a.get('href')
                            if article_url and article_url != '#':
                                await process_article(client, article_url, category_path)

if __name__ == "__main__":
    asyncio.run(main())
