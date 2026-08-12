# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pymupdf4llm",
#     "pymupdf",
#     "pillow",
#     "google-genai",
#     "tqdm"
# ]
# ///

import os
import re
import glob
import sys
import argparse
import time
import pymupdf4llm
import pymupdf as fitz
from PIL import Image
from google import genai
from tqdm import tqdm

MD_DIR = "dataset/books_pdf/gemini/"
RAW_PDF_DIR = "dataset/books_pdf/raw/"
MODEL_NAME = "gemini-3.5-flash-lite"

PROMPT = """Ти - експерт з конвертації технічних підручників у сучасний Markdown.
Твоє завдання: витягти текст з цього зображення сторінки з максимальним збереженням форматування.
Суворо дотримуйся таких правил:
1. Текст: Розпізнай увесь текст, зберігаючи абзаци.
2. КОЛОНТИТУЛИ: Ігноруй номери сторінок та повторювані назви книги/авторів нагорі чи внизу сторінки.
3. Код: ОБОВ'ЯЗКОВО обгорни програмний код у блоки (```мова ... ```). Збережи всі відступи!
4. Формули: Всі математичні формули пиши у форматі LaTeX ($$ або $).
5. БЛОК-СХЕМИ ТА ДІАГРАМИ (Векторні): Якщо бачиш блок-схему, згенеруй її у форматі Mermaid.js. 
6. ОПИС РАСТРОВИХ ЗОБРАЖЕНЬ: Якщо ти вирішив вставити посилання на растрову картинку, ОБОВ'ЯЗКОВО напиши розгорнутий текстовий опис її вмісту (alt-text) всередині квадратних дужок `![Детальний опис...](шлях)`.
Не додавай жодних своїх коментарів до тексту, повертай лише розпізнаний контент.
"""

def find_pdf(pdf_name):
    for root, dirs, files in os.walk(RAW_PDF_DIR):
        if pdf_name in files:
            return os.path.join(root, pdf_name)
    return None

def process_md_file(md_path, keys):
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    if not content: return
        
    lines = content.split('\n')
    match = re.match(r"^#\s+(.+?\.pdf)$", lines[0].strip(), re.IGNORECASE)
    if not match: return
        
    pdf_name = match.group(1)
    
    error_pattern = r"> \[!ERROR\] \[MISSING_PAGE_(\d+)_[^\]]+\][^\n]*"
    missing_pages = re.findall(error_pattern, content)
    
    if not missing_pages: return
        
    print(f"\n📖 {os.path.basename(md_path)}: Знайдено {len(missing_pages)} пропущених сторінок.")
    
    pdf_path = find_pdf(pdf_name)
    if not pdf_path:
        print(f"❌ PDF '{pdf_name}' не знайдено.")
        return

    doc = fitz.open(pdf_path)
    progress_bar = tqdm(total=len(missing_pages), desc="Відновлення")
    
    key_idx = 0
    client = genai.Client(api_key=keys[key_idx])

    def replacer(match_obj):
        nonlocal key_idx, client
        page_num = int(match_obj.group(1))
        page_index = page_num - 1
        
        try:
            # Спроба 1: Gemini API
            page = doc.load_page(page_index)
            matrix = fitz.Matrix(2.0, 2.0)
            pix = page.get_pixmap(matrix=matrix)
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            
            response = client.models.generate_content(model=MODEL_NAME, contents=[PROMPT, img])
            page_md = response.text.strip()
            progress_bar.update(1)
            time.sleep(2)
            return f"\n\n<!-- ВІДНОВЛЕНО ЧЕРЕЗ GEMINI (Стор. {page_num}) -->\n{page_md}\n<!-- КІНЕЦЬ ВІДНОВЛЕННЯ -->\n\n"
            
        except Exception as e:
            err = str(e).lower()
            if "429" in err or "quota" in err or "exhausted" in err:
                # Ротація ключа при ліміті
                key_idx = (key_idx + 1) % len(keys)
                client = genai.Client(api_key=keys[key_idx])
                progress_bar.update(1)
                print(f"\n⚠️ Ліміт на ключі, перемкнулись на інший. Сторінку {page_num} пропущено, перезапустіть скрипт пізніше.")
                return match_obj.group(0)
            else:
                # Якщо Gemini відхилив через цензуру (400), використовуємо локальний fallback!
                print(f"\n🛡️ Gemini відхилив сторінку {page_num} (Цензура/Помилка: {e}). Використовую локальний PyMuPDF4LLM...")
                try:
                    local_md = pymupdf4llm.to_markdown(pdf_path, pages=[page_index])
                    progress_bar.update(1)
                    return f"\n\n<!-- ВІДНОВЛЕНО ЛОКАЛЬНО (Стор. {page_num}) -->\n{local_md.strip()}\n<!-- КІНЕЦЬ ВІДНОВЛЕННЯ -->\n\n"
                except Exception as local_e:
                    progress_bar.update(1)
                    print(f"\n❌ Локальне відновлення теж впало на стор {page_num}: {local_e}")
                    return match_obj.group(0)

    new_content = re.sub(error_pattern, replacer, content)
    doc.close()
    progress_bar.close()

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(new_content)
        
    print(f"✅ Готово!\n")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--keys", nargs="+", default=[], help="Ключі Gemini API")
    args = parser.parse_args()
    
    keys = args.keys
    if not keys:
        env_keys = os.environ.get("GEMINI_API_KEYS")
        if env_keys:
            keys = [k.strip() for k in env_keys.split(",") if k.strip()]
            
    if not keys:
        print("❌ Передайте API ключі через --keys або GEMINI_API_KEYS")
        sys.exit(1)
        
    md_files = glob.glob(os.path.join(MD_DIR, "*.md"))
    for md_path in md_files:
        process_md_file(md_path, keys)

if __name__ == "__main__":
    main()
