import requests
from bs4 import BeautifulSoup
import markdownify
import os
import re
import sys

def fetch_and_clean(url, output_path, site_type):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    
    if site_type == 'dou':
        article = soup.find('article', class_='b-typo')
        if not article:
            article = soup.find('div', class_='b-post-content')
        if article:
            for tag in article.find_all(['script', 'form', 'style']):
                tag.decompose()
            md = markdownify.markdownify(str(article), heading_style="ATX")
        else:
            md = markdownify.markdownify(response.text, heading_style="ATX")
        md = re.split(r'Сподобалась стаття\?', md, flags=re.IGNORECASE)[0]
        md = re.split(r'Підписуйтесь на автора', md, flags=re.IGNORECASE)[0]
        md = re.split(r'<a name=\"comments\"></a>', md)[0]
        md = re.split(r'class=\"b-comments\"', md)[0]
        
    else:
        # Generic
        article = soup.find('article') or soup.find('main')
        if article:
            for tag in article.find_all(['script', 'style', 'nav', 'header', 'footer']):
                tag.decompose()
            md = markdownify.markdownify(str(article), heading_style="ATX")
        else:
            md = markdownify.markdownify(response.text, heading_style="ATX")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        title = soup.find('title')
        if title:
            f.write(f"# {title.text.strip()}\n\n")
        f.write(md.strip())
        
    print(f"Successfully processed {url} -> {output_path}")

if __name__ == "__main__":
    if len(sys.argv) == 4:
        fetch_and_clean(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Usage: python fetch_articles.py <url> <output_path> <site_type>")
