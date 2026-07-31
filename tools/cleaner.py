import os
import glob
import re

DATASET_DIR = "../qalight"

def clean_markdown_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if len(lines) < 10:
        return True # Probably already cleaned

    title_line = lines[0].strip()
    if not title_line.startswith("# "):
        return False
    
    title_text = title_line[2:].strip()
    
    header_end_idx = 0
    payload_start_idx = -1
    payload_end_idx = len(lines)

    # 1. Знаходимо кінець мета-шапки
    for i, line in enumerate(lines):
        if line.strip() == "---":
            header_end_idx = i + 1
            break
            
    # 2. Знаходимо початок статті (шукаємо title_text)
    for i in range(header_end_idx, len(lines)):
        line = lines[i].strip()
        # Очищуємо від базових символів розмітки
        clean_line = re.sub(r'^[#*\s-]+', '', line).strip()
        # Важливо: ми перевіряємо, чи рядок є ТОЧНО назвою статті (без URL-посилань всередині)
        # Або якщо він починається з назви статті, але не містить '](http'
        if clean_line.lower() == title_text.lower() or (title_text.lower() in clean_line.lower() and "](" not in clean_line):
            payload_start_idx = i
            break
            
    # 3. Знаходимо кінець статті (шукаємо футер зверху вниз від payload)
    end_markers = ["Обери курс для навчання", "Зв'язатися з нами", "Адреса: м. Київ"]
    if payload_start_idx != -1:
        for i in range(payload_start_idx, len(lines)):
            for marker in end_markers:
                if marker in lines[i]:
                    payload_end_idx = i
                    break
            if payload_end_idx != len(lines):
                break
                
    if payload_start_idx == -1 or payload_end_idx == len(lines):
        return False # Скрипт сумнівається

    # Трохи підчищаємо порожні рядки та зірочки перед футером
    while payload_end_idx > payload_start_idx and (lines[payload_end_idx-1].strip() == "" or lines[payload_end_idx-1].strip() == "*" or lines[payload_end_idx-1].startswith("* [")):
        payload_end_idx -= 1

    clean_lines = lines[:header_end_idx] + ["\n"] + lines[payload_start_idx:payload_end_idx]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(clean_lines)
    
    return True

def main():
    search_pattern = os.path.join(DATASET_DIR, "**", "*.md")
    md_files = glob.glob(search_pattern, recursive=True)
    
    difficult_files = []
    
    for filepath in md_files:
        success = clean_markdown_file(filepath)
        if not success:
            difficult_files.append(filepath)
            
    if difficult_files:
        with open("difficult_files.txt", "w") as f:
            for df in difficult_files:
                f.write(df + "\n")
        print(f"Автоматично очищено {len(md_files) - len(difficult_files)} файлів.")
        print(f"Знайдено {len(difficult_files)} нестандартних файлів, залишено для AI-чистки.")
    else:
        print(f"Всі {len(md_files)} файлів ідеально очищено автоматично!")

if __name__ == "__main__":
    main()
