import argparse
import os
import urllib.request
from bs4 import BeautifulSoup
import markdownify
import re

def fetch_and_clean_qatestlab_article(url: str, output_path: str):
    print(f"[*] Fetching QATestLab article: {url}")
    
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
    except Exception as e:
        print(f"[!] Error fetching {url}: {e}")
        return False

    soup = BeautifulSoup(html, 'html.parser')

    # Extract title from outside the content container
    title_tag = soup.find('h1', class_='post_title')
    title_md = f"# {title_tag.get_text(strip=True)}\n\n" if title_tag else ""

    # Specific container for QATestLab blog posts
    article = soup.find('div', class_='stm_archive_product_inner_grid_content')
    if not article:
        print("[!] Error: Could not find 'stm_archive_product_inner_grid_content' container.")
        return False

    unwanted_tags = ['script', 'style', 'nav', 'header', 'footer', 'aside', 'iframe']
    for tag in article.find_all(unwanted_tags):
        tag.decompose()

    md = markdownify.markdownify(str(article), heading_style="ATX", code_language="c")
    md = title_md + md
    md = re.sub(r'\n{3,}', '\n\n', md)

    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md.strip() + "\n")

    print(f"[+] Success! Clean Markdown saved to: {output_path}")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch QATestLab articles and convert to clean Markdown.")
    parser.add_argument("url", help="Direct URL to the article")
    parser.add_argument("output", help="Path to save the Markdown file")
    
    args = parser.parse_args()
    fetch_and_clean_qatestlab_article(args.url, args.output)
