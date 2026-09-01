import os
import re

def clean_words(t):
    t = re.sub(r'```mermaid.*?```', '', t, flags=re.DOTALL)
    t = re.sub(r'```.*?```', '', t, flags=re.DOTALL)
    words = re.findall(r'[a-zA-Zа-яА-ЯіІїЇєЄ0-9]+', t.lower())
    return set(words), len(words)

def is_same_slide_family(text1, text2):
    w1, l1 = clean_words(text1)
    w2, l2 = clean_words(text2)
    
    if l1 == 0 or l2 == 0: return True
    
    # Calculate Jaccard similarity
    intersection = w1.intersection(w2)
    union = w1.union(w2)
    
    # If one is almost completely a subset of another's words
    if len(intersection) / len(w1) > 0.7 or len(intersection) / len(w2) > 0.7:
        return True
        
    return False

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    parts = re.split(r'(?m)^(#+\s+.*)$', content)
    if len(parts) < 3: return False
        
    sections = [("", parts[0])]
    for i in range(1, len(parts), 2):
        header_line = parts[i]
        text = parts[i+1] if i+1 < len(parts) else ""
        title = re.sub(r'^#+\s*', '', header_line).strip().lower()
        sections.append((title, header_line + "\n" + text))
        
    filtered = []
    i = 0
    while i < len(sections):
        title = sections[i][0]
        full_text = sections[i][1]
        
        if title == "":
            filtered.append(full_text)
            i += 1
            continue
            
        family = [full_text]
        j = i + 1
        
        while j < len(sections) and sections[j][0] == title:
            # For slide duplicates, they usually all share the same words
            if is_same_slide_family(family[-1], sections[j][1]):
                family.append(sections[j][1])
                j += 1
            else:
                break
                
        # Best section is the one with the most actual words (excluding mermaid)
        best_section = max(family, key=lambda x: clean_words(x)[1])
        filtered.append(best_section)
        i = j
        
    new_content = "".join(filtered)
    new_content = re.sub(r'\n{3,}', '\n\n', new_content)
    
    if new_content.strip() != content.strip():
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    parsed_dir = "dataset/pptx_doc/popeliuha/parsed/"
    count = 0
    for filename in os.listdir(parsed_dir):
        if filename.endswith(".md"):
            if process_file(os.path.join(parsed_dir, filename)):
                count += 1
                print(f"Removed duplicates in {filename}")
    print(f"Total files cleaned: {count}")

if __name__ == "__main__":
    main()
