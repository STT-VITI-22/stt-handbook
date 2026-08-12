import re

def analyze_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        return
    
    # Split content by lines
    lines = content.split('\n')
    
    in_code_block = False
    last_code_end = -100
    last_code_end_line = -100
    
    print(f"--- Аналіз файлу: {filename} ---")
    
    for i, line in enumerate(lines):
        if line.strip().startswith('```'):
            if not in_code_block:
                in_code_block = True
                
                # Check if this new code block is very close to the previous one
                # and separated mostly by page markers
                distance = i - last_code_end_line
                if 0 < distance < 15:
                    # check what is between them
                    between_text = "\n".join(lines[last_code_end_line+1:i]).strip()
                    if "Сторінка" in between_text or "Page" in between_text or len(between_text) < 20:
                        print(f"⚠️ Можливий розрив коду між рядками {last_code_end_line+1} та {i+1}")
                        print(f"   Між ними текст: {repr(between_text)}")
                        print(f"   Початок нового блоку: {line}")
                        print("-" * 40)
            else:
                in_code_block = False
                last_code_end_line = i

analyze_file("dataset/books_pdf/gemini/testyvan_gemini.md")
analyze_file("dataset/books_pdf/gemini/missing_pages_perfect.md")
