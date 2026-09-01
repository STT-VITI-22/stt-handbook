import os
import re
import urllib.parse

parsed_dir = "dataset/pptx_doc/popeliuha/parsed/"
count = 0

def replace_spaces(match):
    alt_text = match.group(1)
    url = match.group(2)
    # only encode if it's a local path and has spaces
    if " " in url:
        # Properly encode spaces
        encoded_url = url.replace(" ", "%20")
        return f"![{alt_text}]({encoded_url})"
    return match.group(0)

for filename in os.listdir(parsed_dir):
    if not filename.endswith(".md"): continue
    
    filepath = os.path.join(parsed_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    new_content = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', replace_spaces, content)
    
    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        count += 1
        
print(f"Fixed image spaces in {count} files.")
