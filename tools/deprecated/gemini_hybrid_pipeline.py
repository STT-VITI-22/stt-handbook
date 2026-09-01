import fitz  # PyMuPDF
import google.generativeai as genai
import time
from pathlib import Path
from PIL import Image
import io
import re

# ================= НАЛАШТУВАННЯ =================
API_KEY = "ВАШ_GEMINI_API_КЛЮЧ"  # Вставте свій ключ сюди!
PDF_PATH = "testyvan.pdf"
OUTPUT_MD = "testyvan_perfect.md"

genai.configure(api_key=API_KEY)
# Використовуємо Flash - вона найшвидша, найдешевша і має Vision
model = genai.GenerativeModel('gemini-1.5-flash-latest')

def needs_vlm_correction(text: str) -> bool:
    """
    Евристичний фільтр. Шукає ознаки коду або складних формул.
    Якщо знаходить - повертає True (треба відправити сторінку у VLM).
    """
    # Ключові слова для C++ / C# / Java / логіки
    code_patterns = [
        r'\bpublic\b', r'\bvoid\b', r'\bint\b\s+[a-zA-Z]', 
        r'\bif\s*\(', r'\bswitch\s*\(', r'\bcase\s+\d',
        r'\{', r'\}'
    ]
    math_patterns = [
        r'f\s*=\s*f', r'A\s*\*\s*3', r'->'
    ]
    
    combined_pattern = re.compile('|'.join(code_patterns + math_patterns))
    return bool(combined_pattern.search(text))

def process_pdf(pdf_path: str, output_path: str):
    doc = fitz.open(pdf_path)
    final_markdown = []
    
    print(f"Починаємо обробку {pdf_path}. Всього сторінок: {len(doc)}")
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        raw_text = page.get_text("text")
        
        print(f"\n--- Сторінка {page_num + 1} ---")
        
        if needs_vlm_correction(raw_text):
            print("Знайдено код/формули. Відправляємо зображення у Gemini...")
            
            # Рендеримо сторінку в картинку
            pix = page.get_pixmap(dpi=150)
            img_data = pix.tobytes("png")
            img = Image.open(io.BytesIO(img_data))
            
            # Промпт для моделі
            prompt = (
                "Ти - експерт з оцифрування технічних підручників. "
                "Ось зображення сторінки з підручника. "
                "Витягни весь текст у форматі Markdown. "
                "Особлива увага: якщо бачиш програмний код, обгорни його у блок ```cpp ... ``` і збережи правильні відступи. "
                "Якщо бачиш формули, використовуй Markdown/LaTeX форматування. "
                "Не додавай ніяких своїх коментарів, поверни ТІЛЬКИ витягнутий Markdown текст."
            )
            
            try:
                response = model.generate_content([prompt, img])
                page_md = response.text
                final_markdown.append(page_md)
                
                # Захист від лімітів API (15 запитів на хвилину)
                print("Успіх! Чекаємо 4 секунди (ліміти API)...")
                time.sleep(4)
                
            except Exception as e:
                print(f"Помилка API на сторінці {page_num + 1}: {e}")
                # Fallback: беремо сирий текст
                final_markdown.append(raw_text)
                
        else:
            print("Звичайна текстова сторінка. Витягуємо локально (швидко).")
            # Для звичайного тексту беремо сирий текст 
            # (Тут в ідеалі можна використати PyMuPDF4LLM для збереження таблиць)
            final_markdown.append(raw_text)
            
        # Автозбереження після кожної сторінки
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n\n---\n\n".join(final_markdown))
            
    print(f"\nГотово! Ідеальний Markdown збережено у {output_path}")

if __name__ == "__main__":
    process_pdf(PDF_PATH, OUTPUT_MD)
