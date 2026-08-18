import os
import argparse
from bs4 import BeautifulSoup
import markdownify
import re

def parse_medium_html(input_path, output_path):
    if not os.path.exists(input_path):
        print(f"Error: Input file '{input_path}' not found.")
        return

    with open(input_path, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    
    article = soup.find('article')
    if not article:
        print(f"Warning: No <article> tag found in {input_path}. Falling back to body.")
        article = soup.find('body')
        
    if article:
        # Clean out typical Medium fluff
        for tag in article.find_all(['script', 'style', 'nav', 'header', 'footer']):
            tag.decompose()
            
        for tag in article.find_all(['a', 'div', 'span', 'p']):
            text = tag.get_text(strip=True).lower()
            if text in ['listen', 'share', 'more from', 'read more', 'open in app', 'sign up', 'sign in']:
                tag.decompose()
                
        # Fix missing images (lazy loading bypass via <noscript>)
        for img in article.find_all('img'):
            noscript = img.find_next_sibling('noscript')
            if noscript and noscript.find('img'):
                real_img = noscript.find('img')
                if real_img.get('src'):
                    img['src'] = real_img['src']
            elif img.parent and img.parent.name == 'picture':
                source = img.parent.find('source')
                if source and source.get('srcset'):
                    img['src'] = source.get('srcset').split(',')[0].split(' ')[0]
            
            if not img.get('src') and img.get('srcset'):
                img['src'] = img.get('srcset').split(',')[0].split(' ')[0]
                
        for button in article.find_all('button'):
            button.decompose()
            
        md = markdownify.markdownify(str(article), heading_style="ATX")
        
        cleaned_lines = []
        capture = False
        for line in md.split('\n'):
            line_stripped = line.strip()
            if line_stripped.startswith('# '):
                capture = True
            
            if not capture:
                continue
                
            if line_stripped in ['Share', 'Press enter or click to view image in full size', '--']:
                continue
            if 'min read' in line_stripped:
                continue
            if 'Listen' in line_stripped and line_stripped.startswith('['):
                continue
                
            cleaned_lines.append(line)
            
        final_md = '\n'.join(cleaned_lines)
        final_md = re.sub(r'\n{3,}', '\n\n', final_md)
        
        os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(final_md.strip() + "\n")
            
        print(f"Success! Medium article saved to: {output_path}")
    else:
        print(f"Error: Could not parse {input_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse raw Medium HTML into clean Markdown (bypassing lazy load & fluff).")
    parser.add_argument("input", help="Path to the raw HTML file (e.g. 'article.html')")
    parser.add_argument("output", help="Path for the output Markdown file (e.g. 'dataset/articles/medium/article.md')")
    args = parser.parse_args()
    
    parse_medium_html(args.input, args.output)
