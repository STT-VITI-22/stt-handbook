import os
import re
import urllib.parse
from pathlib import Path

def check_links():
    repo_root = Path(__file__).parent.parent.parent
    md_files = list(repo_root.rglob('*.md'))
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    
    broken_links = []
    
    for md_path in md_files:
        if '.git' in md_path.parts or '.venv' in md_path.parts:
            continue
            
        try:
            with open(md_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            print(f"Failed to read as UTF-8: {md_path}")
            continue
            
        links = link_pattern.findall(content)
        for text, link in links:
            if link.startswith('http') or link.startswith('data:') or link.startswith('mailto:') or link.startswith('#'):
                continue
                
            parsed_link = urllib.parse.unquote(link)
            file_part = parsed_link.split('#')[0]
            
            if not file_part:
                continue
                
            base_dir = md_path.parent
            target_path = (base_dir / file_part).resolve()
            
            if not target_path.exists():
                broken_links.append({
                    'file': str(md_path.relative_to(repo_root)),
                    'text': text,
                    'link': link,
                    'resolved': str(target_path)
                })
                
    from collections import defaultdict
    grouped = defaultdict(list)
    for b in broken_links:
        grouped[b['file']].append(b)
        
    if grouped:
        print(f"Знайдено {len(broken_links)} битих внутрішніх посилань:\n")
        for file, breaks in grouped.items():
            print(f"\n📄 У файлі: {file}")
            for b in breaks:
                print(f"   ❌ Текст: [{b['text']}]")
                print(f"      Лінк: {b['link']}")
    else:
        print("Внутрішніх битих посилань не знайдено!")

if __name__ == '__main__':
    check_links()
