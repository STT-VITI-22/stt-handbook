import os
import glob
import re
import shutil

dir_path = 'dataset/youtube/popeliuha'
files = glob.glob(os.path.join(dir_path, '*.md'))

def get_clean_name(title):
    t = title.replace('#', 'Sharp')
    t = t.replace('+', 'Plus')
    t = t.replace('&', 'and')
    t = re.sub(r'[\.\,\:\|/\\]', '-', t)
    t = re.sub(r"[\(\)\'\?\😱\u200b]", "", t)
    t = re.sub(r'\s+', '_', t.strip())
    t = re.sub(r'-+', '-', t)
    t = re.sub(r'_+', '_', t)
    t = t.strip('-_') # remove leading/trailing dashes or underscores
    return t

def get_category(title):
    t_lower = title.lower()
    if 'istqb' in t_lower: return 'ISTQB'
    if 'c#' in t_lower or 'c sharp' in t_lower or 'csharp' in t_lower: return 'CSharp_Automation'
    if 'mysql' in t_lower or 'бази даних' in t_lower or 'sql' in t_lower: return 'MySQL'
    if 'git' in t_lower or 'github' in t_lower or 'source tree' in t_lower: return 'Git'
    if any(kw in t_lower for kw in ['scrum', 'agile', 'trello', 'jira', 'confluence', 'devops']): return 'Agile_and_Management'
    if any(kw in t_lower for kw in ['api', 'postman', 'fiddler', 'selenium', 'jmeter', 'xml', 'json', 'dev tools', 'девтулз', 'xpath']): return 'Tools_and_API'
    if any(kw in t_lower for kw in ['тест дизайн', 'boundary', 'equivalence', 'еквівалентн', 'decision', 'покриття', 'pairwise', 'use-case', 'state-transition', 'boundary values']): return 'Test_Design_Techniques'
    if any(kw in t_lower for kw in ['роботу', 'співбесід', 'резюме', 'фріланс', 'upwork', 'outsource', 'product', 'linkedin', 'англійськ']): return 'Career_and_Interviews'
    return 'QA_Fundamentals'

processed = 0
for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    first_line = content.split('\n')[0].strip()
    if first_line.startswith('# '):
        original_title = first_line[2:]
        
        category = get_category(original_title)
        clean_name = get_clean_name(original_title)
        
        cat_dir = os.path.join(dir_path, category)
        os.makedirs(cat_dir, exist_ok=True)
        
        new_path = os.path.join(cat_dir, f"{clean_name}.md")
        
        with open(new_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        os.remove(fpath)
        processed += 1

print(f"Успішно перейменовано та розсортовано файлів: {processed}")
