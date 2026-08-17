import re

filename = "dataset/books_pdf/gemini/testyvan_gemini.md"
with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to find the gap between two code blocks spanning a page.
# It matches: 
# 1. ``` (the end of the first code block)
# 2. any whitespace (newlines)
# 3. an optional page number (like 161)
# 4. any whitespace
# 5. the page marker <!-- Сторінка 162 --> or <!-- Відновлена Сторінка 162 -->
# 6. any whitespace
# 7. ``` and optional language specifier (like cpp)
# 8. a trailing newline
pattern = re.compile(r'```\s*(?:[0-9]+\s*)?<!-- (?:Відновлена )?Сторінка ([0-9]+) -->\s*```[a-zA-Z]*\n', re.MULTILINE)

matches = pattern.finditer(content)
count = 0

print("--- ЗНАЙДЕНІ РОЗРИВИ ---")
for match in matches:
    page_num = match.group(1)
    gap_text = match.group(0)
    print(f"Злиття на сторінці {page_num}:")
    print("Видаляється текст:")
    print(repr(gap_text))
    print("-" * 30)
    count += 1

# Replace with a single newline to just merge the code blocks smoothly
new_content = pattern.sub('\n', content)

with open(filename, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"\nУспішно об'єднано {count} розірваних блоків коду!")
