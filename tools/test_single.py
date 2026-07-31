import os
import asyncio
import httpx
from bs4 import BeautifulSoup
from markdownify import markdownify as md

async def test_parse():
    url = "https://qalight.ua/baza-znaniy/funktsionalne-testuvannya/"
    print(f"Ізольоване тестування уніфікованого парсера на: {url}")
    
    async with httpx.AsyncClient(timeout=15.0) as client:
        response = await client.get(url, follow_redirects=True)
        soup = BeautifulSoup(response.text, 'lxml')
        
        # 1. Екстракція заголовка
        title_tag = soup.find('h1')
        title_ukr = title_tag.get_text(strip=True) if title_tag else (soup.title.string.split('-')[0].strip() if soup.title else "Без назви")
        
        # 2. Екстракція виключно цільового пейлоаду (уніфікований підхід)
        content_container = soup.find('div', class_='single-knowledge-base-content')
        
        if not content_container:
            print("ПОМИЛКА: Не знайдено контейнер single-knowledge-base-content!")
            return
            
        # 3. Видалення технічних артефактів (JS/CSS/Iframes)
        for unwanted in content_container.find_all(['script', 'style', 'noscript', 'meta', 'link', 'iframe']):
            unwanted.decompose()
            
        # 3.1. Видалення специфічних для QALight вбудованих меню (сайдбари, які лежать всередині контенту)
        for sidebar in content_container.find_all('div', class_=['sidebar', 'sidebar-mobile', 'menu-block']):
            sidebar.decompose()
            
        # 4. Трансформація DOM у Markdown
        markdown_text = md(str(content_container), heading_style="ATX")
        
        # Збереження
        os.makedirs("test_output", exist_ok=True)
        out_path = "test_output/test_functional.md"
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(f"# {title_ukr}\n\n{markdown_text}")
            
        print(f"Успішно! Збережено в {out_path}.")

if __name__ == "__main__":
    asyncio.run(test_parse())
