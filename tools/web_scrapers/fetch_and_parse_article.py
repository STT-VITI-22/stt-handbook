import argparse
import os
import re
import urllib.request
from bs4 import BeautifulSoup
import markdownify

def fetch_and_clean_article(url: str, output_path: str):
    """
    Fetches an HTML article from a given URL and converts it into clean Markdown.
    Removes headers, footers, scripts, styles, and navigation menus.
    """
    print(f"[*] Fetching: {url}")
    
    # Set a standard User-Agent to avoid basic blocks
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
    except Exception as e:
        print(f"[!] Error fetching {url}: {e}")
        return False

    soup = BeautifulSoup(html, 'html.parser')
    
    # Attempt to find the main content body
    # Engineering blogs typically use <article>, <main>, or id="post-page"
    article = soup.find('article')
    if not article:
        article = soup.find(id='post-page')
    if not article:
        article = soup.find('main')
    if not article:
        print("[!] Warning: Could not find <article> or <main>. Falling back to <body>.")
        article = soup.find('body')

    if article:
        # 1. Decompose unwanted tags (web garbage)
        unwanted_tags = ['script', 'style', 'nav', 'header', 'footer', 'aside', 'iframe']
        for tag in article.find_all(unwanted_tags):
            tag.decompose()
            
        # 2. Convert to Markdown using markdownify
        # heading_style="ATX" ensures # instead of --- under headers
        md = markdownify.markdownify(str(article), heading_style="ATX", code_language="c")
        
        # 3. Post-process to remove excessive newlines
        md = re.sub(r'\n{3,}', '\n\n', md)
        
        # 4. Save to file
        os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(md.strip() + "\n")
            
        print(f"[+] Success! Clean Markdown saved to: {output_path}")
        return True
    else:
        print(f"[!] Error: HTML parsing failed for {url}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch engineering articles (e.g. Memfault, Hackaday) and convert to clean Markdown.")
    parser.add_argument("url", help="Direct URL to the article")
    parser.add_argument("output", help="Path to save the Markdown file (e.g. dataset/articles/source/name.md)")
    
    args = parser.parse_args()
    fetch_and_clean_article(args.url, args.output)
