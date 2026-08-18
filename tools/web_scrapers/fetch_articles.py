import requests
from bs4 import BeautifulSoup
import markdownify
import os
import re
import argparse

def fetch_and_clean(url, output_path, site_type):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }
    print(f"Fetching: {url}")
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
        # Generic fallback
        article = soup.find('article') or soup.find('main')
        if article:
            for tag in article.find_all(['script', 'style', 'nav', 'header', 'footer']):
                tag.decompose()
            md = markdownify.markdownify(str(article), heading_style="ATX")
        else:
            md = markdownify.markdownify(response.text, heading_style="ATX")

    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        title = soup.find('title')
        if title:
            f.write(f"# {title.text.strip()}\n\n")
        f.write(md.strip() + "\n")
        
    print(f"Success! Article saved to: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch an article from a URL and convert it to clean Markdown.")
    parser.add_argument("url", help="The URL of the article to fetch")
    parser.add_argument("output", help="Path for the output Markdown file (e.g. 'dataset/articles/dou/article.md')")
    parser.add_argument("--type", choices=['dou', 'generic'], default='generic', 
                        help="Site type to apply specific cleanup rules. Use 'dou' for dou.ua forums, or 'generic' for others. (default: generic)")
    
    args = parser.parse_args()
    fetch_and_clean(args.url, args.output, args.type)
