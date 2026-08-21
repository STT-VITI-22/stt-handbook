import os
import glob

def fix_paths():
    replacements = {
        "dataset/dou": "dataset/articles/dou",
        "dataset/qalight": "dataset/articles/qalight",
        "dataset/QA_Bible": "dataset/articles/QA_Bible"
    }
    
    # Let's find all md and py files
    files = []
    for ext in ["**/*.md", "**/*.py"]:
        files.extend(glob.glob(ext, recursive=True))
        
    for file in files:
        if ".git/" in file or "tools/fix_paths.py" in file:
            continue
            
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content
        for old, new in replacements.items():
            # Replace only exact directory matches (e.g. dataset/dou or dataset/dou/something)
            new_content = new_content.replace(old, new)
            
        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated paths in {file}")

if __name__ == "__main__":
    fix_paths()
