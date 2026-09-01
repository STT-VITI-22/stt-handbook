import re

def find_broken_blocks(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except: return

    print(f"\n--- Аналіз файлу: {filename} ---")
    
    # regex to find ``` closing block, some small text with 'Сторінка', and ``` opening block
    # We look for:
    # 1. ``` (end of block)
    # 2. Up to 200 characters of non-code-block text containing "Сторінка"
    # 3. ``` (start of new block)
    
    pattern = re.compile(r'```[^\n]*\n(.*?)```[a-zA-Z]*\n', re.DOTALL)
    
    # Actually, it's easier to iterate through the text and find ` ``` ` boundaries
    parts = content.split('```')
    
    # parts[0] is text, parts[1] is code, parts[2] is text, parts[3] is code...
    # So odd indices are code blocks, even indices are text between code blocks.
    
    found = False
    for i in range(2, len(parts), 2):
        text_between = parts[i]
        
        # Check if the text between two code blocks is very short and contains a page break
        if "Сторінка" in text_between and text_between.count('\n') < 8:
            print(f"⚠️ Знайдено розірваний блок коду!")
            print(f"Текст між блоками:\n{text_between.strip()}")
            print("-" * 40)
            found = True
            
    if not found:
        print("✅ Розірваних блоків коду на стику сторінок не знайдено.")

find_broken_blocks("dataset/books_pdf/gemini/testyvan_gemini.md")
find_broken_blocks("dataset/books_pdf/gemini/missing_pages_perfect.md")
