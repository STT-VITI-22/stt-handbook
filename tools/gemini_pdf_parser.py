# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pymupdf",
#     "pillow",
#     "google-genai",
#     "tqdm",
# ]
# ///

import os
import sys
import time
import argparse
import queue
import threading
import json
from datetime import date
import pymupdf as fitz
from PIL import Image
from google import genai
from tqdm import tqdm

# ================= НАЛАШТУВАННЯ =================
DEFAULT_OUTPUT_DIR = "/home/liulmiti/workspace/22_dep/stt/dataset/dataset/books_pdf/gemini"
# 15 RPM = 1 запит на 4 сек. Ми слідкуємо, щоб між ПОЧАТКОМ запитів проходило мінімум 4.1 сек.
DELAY_SECONDS = 4.1 
DAILY_LIMIT = 500
MODEL_NAME = "gemini-3.5-flash-lite"  # Хардкод найшвидшої моделі з квотою 500 RPD
# =================================================

PROMPT = """Ти - експерт з конвертації технічних підручників у сучасний Markdown.
Твоє завдання: витягти текст з цього зображення сторінки з максимальним збереженням форматування.
Суворо дотримуйся таких правил:

1. Текст: Розпізнай увесь текст, зберігаючи абзаци.
2. КОЛОНТИТУЛИ: Ігноруй номери сторінок та повторювані назви книги/авторів нагорі чи внизу сторінки.
3. Код: ОБОВ'ЯЗКОВО обгорни програмний код у блоки (```мова ... ```). Збережи всі відступи!
4. Формули: Всі математичні формули пиши у форматі LaTeX ($$ або $).
5. БЛОК-СХЕМИ ТА ДІАГРАМИ (Векторні): Якщо бачиш блок-схему, згенеруй її у форматі Mermaid.js (```mermaid ... ```). Правила Mermaid: використовуй лапки для тексту з пробілами або дужками. 
⚠️ КРИТИЧНЕ ПРАВИЛО ДЛЯ ДІАГРАМ: Якщо на сторінці УЖЕ є растрова картинка цієї ж схеми (шляхи до яких я передав у системному повідомленні), СУВОРО ВИБЕРИ ТІЛЬКИ ОДИН ВАРІАНТ: АБО встав посилання на растрову картинку, АБО згенеруй Mermaid код. НІКОЛИ НЕ ВИВОДЬ ОБИДВА ДЛЯ ОДНІЄЇ І ТІЄЇ Ж СХЕМИ.
6. ОПИС РАСТРОВИХ ЗОБРАЖЕНЬ: Якщо ти вирішив вставити посилання на растрову картинку, ОБОВ'ЯЗКОВО напиши розгорнутий текстовий опис її вмісту (alt-text) всередині квадратних дужок `![Детальний опис того, що саме намальовано чи показано на картинці](шлях)`. Це критично важливо для векторного пошуку!

Не додавай жодних своїх коментарів до тексту, повертай лише розпізнаний контент.
"""

NAME_PROMPT = """Проаналізуй ці перші сторінки книги.
Згенеруй унікальну, URL-friendly назву файлу для цієї книги. Формат: AuthorSurname_Year_CoreKeyword.md
Не використовуй кирилицю. Виведи ТІЛЬКИ назву файлу (без зайвого тексту)."""

class KeyUsageDB:
    def __init__(self, db_path):
        self.db_path = db_path
        self.lock = threading.Lock()
        self.usage = self._load()
        
    def _load(self):
        if os.path.exists(self.db_path):
            try:
                with open(self.db_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
        return {}
        
    def _save(self):
        with open(self.db_path, "w", encoding="utf-8") as f:
            json.dump(self.usage, f, indent=4)
            
    def mask_key(self, api_key):
        if len(api_key) < 12: return api_key
        return api_key[:6] + "..." + api_key[-4:]
            
    def increment(self, api_key):
        today = str(date.today())
        masked = self.mask_key(api_key)
        with self.lock:
            if masked not in self.usage or self.usage[masked].get("date") != today:
                self.usage[masked] = {"date": today, "count": 0}
            self.usage[masked]["count"] += 1
            self._save()
            return self.usage[masked]["count"]
            
    def get_stats(self, api_key):
        today = str(date.today())
        masked = self.mask_key(api_key)
        with self.lock:
            record = self.usage.get(masked, {"date": today, "count": 0})
            if record["date"] != today:
                return 0
            return record["count"]

def generate_filename(pdf_path, keys):
    print(f"🧠 Аналізуємо титульні сторінки для генерації назви (Модель: {MODEL_NAME})...")
    doc = fitz.open(pdf_path)
    pages_to_check = min(3, len(doc))
    images = [NAME_PROMPT]
    matrix = fitz.Matrix(1.5, 1.5)
    for i in range(pages_to_check):
        pix = doc.load_page(i).get_pixmap(matrix=matrix)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        images.append(img)
    doc.close()
    
    for api_key in keys:
        try:
            client = genai.Client(api_key=api_key)
            response = client.models.generate_content(model=MODEL_NAME, contents=images)
            name = response.text.strip().replace("`", "").replace("'", "").replace('"', "")
            if not name.endswith(".md"): name += ".md"
            name = "".join(c for c in name if c.isalnum() or c in "_-.")
            print(f"✨ Згенерована назва: {name}")
            return name
        except Exception:
            continue
    print("⚠️ Генерація назви не вдалася (ключі не відповіли).")
    return "default_book.md"

def get_frequent_xrefs(doc, threshold=5):
    """Знаходить картинки (xrefs), які повторюються на багатьох сторінках (водяні знаки, фони)."""
    xref_counts = {}
    for i in range(len(doc)):
        for img in doc.load_page(i).get_images(full=True):
            xref = img[0]
            xref_counts[xref] = xref_counts.get(xref, 0) + 1
    return {xref for xref, count in xref_counts.items() if count > threshold}

def extract_raster_images(doc, page, page_num, images_dir, ignore_xrefs):
    image_list = page.get_images(full=True)
    saved_images = []
    for img_index, img in enumerate(image_list):
        xref = img[0]
        
        # Фільтр спаму: ігноруємо водяні знаки та фони
        if xref in ignore_xrefs:
            continue
            
        base_image = doc.extract_image(xref)
        
        # Фільтр сміття: ігноруємо картинки-карлики (маркери списків, лінії, іконки)
        width = base_image.get("width", 0)
        height = base_image.get("height", 0)
        if width < 100 or height < 100:
            continue
            
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        image_name = f"page_{page_num}_img_{img_index + 1}.{image_ext}"
        image_path = os.path.join(images_dir, image_name)
        with open(image_path, "wb") as f:
            f.write(image_bytes)
        saved_images.append(image_name)
    return saved_images

def worker_thread(api_key, key_index, page_queue, results_dict, failed_list, pdf_path, images_dir, book_name_no_ext, progress_bar, db, active_threads, ignore_xrefs):
    client = genai.Client(api_key=api_key)
    doc = fitz.open(pdf_path)
    masked_key = db.mask_key(api_key)
    
    # Трекінг часу для розумного сліпу
    last_request_time = 0
    
    while True:
        try:
            page_num = page_queue.get(timeout=2)
        except queue.Empty:
            break
            
        if db.get_stats(api_key) >= DAILY_LIMIT:
            print(f"\n⚠️ Ключ {masked_key} вичерпав денний ліміт ({DAILY_LIMIT}). Потік зупиняється.")
            page_queue.put(page_num)
            break
            
        # Розумний rate-limiting: спимо ТІЛЬКИ якщо з попереднього запиту пройшло менше 4.1 сек
        time_since_last = time.time() - last_request_time
        if time_since_last < DELAY_SECONDS:
            time.sleep(DELAY_SECONDS - time_since_last)
            
        human_page_num = page_num + 1
        page = doc.load_page(page_num)
        saved_images = extract_raster_images(doc, page, human_page_num, images_dir, ignore_xrefs)
        
        matrix = fitz.Matrix(2.0, 2.0)
        pix = page.get_pixmap(matrix=matrix)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        
        dynamic_prompt = PROMPT
        if saved_images:
            relative_image_paths = [f"images/{book_name_no_ext}/{img_name}" for img_name in saved_images]
            dynamic_prompt += f"\n\n[СИСТЕМНЕ ПОВІДОМЛЕННЯ]: На цій сторінці знайдено {len(saved_images)} растрових зображень. Вони збережені тут: {', '.join(relative_image_paths)}. Якщо бачиш їх, обов'язково встав у текст посилання на них у форматі ![Опис](шлях)."

        success = False
        for attempt in range(3):
            last_request_time = time.time() # Оновлюємо таймер перед запитом
            try:
                response = client.models.generate_content(model=MODEL_NAME, contents=[dynamic_prompt, img])
                results_dict[page_num] = response.text.strip()
                db.increment(api_key)
                progress_bar.update(1)
                success = True
                break
            except Exception as e:
                err_msg = str(e).lower()
                if "quota_limit_value': '0'" in err_msg or "billing" in err_msg:
                    print(f"\n💀 Ключ {masked_key} МЕРТВИЙ. Потік зупиняється.")
                    page_queue.put(page_num)
                    active_threads[key_index] = False
                    return 
                elif "429" in err_msg or "exhausted" in err_msg or "quota" in err_msg or "503" in err_msg:
                    time.sleep(5) # Короткий сон, бо інші ключі можуть підстрахувати
                else:
                    failed_list.append(human_page_num)
                    results_dict[page_num] = f"\n\n> [!ERROR] [MISSING_PAGE_{human_page_num}_COPYRIGHT] ({e})\n\n"
                    db.increment(api_key)
                    progress_bar.update(1)
                    success = True
                    break
        
        if not success:
            page_queue.put(page_num)
            time.sleep(10) # Спимо, якщо ключ забанили надовго
            
    active_threads[key_index] = False

def process_pdf(pdf_path, output_dir, keys):
    start_time = time.time()
    print(f"🚀 Запуск FAST-TRACK обробки з {len(keys)} ключами (Модель: {MODEL_NAME})!")
    
    db_path = os.path.join(output_dir, "api_usage.json")
    db = KeyUsageDB(db_path)
    
    print("\n📊 Статистика використання ключів (Ліміт: 1500/день):")
    for idx, key in enumerate(keys):
        used = db.get_stats(key)
        print(f"   Ключ {idx+1} ({db.mask_key(key)}): {used}/{DAILY_LIMIT} запитів сьогодні.")
    print("-" * 50)
    
    filename = generate_filename(pdf_path, keys)
    
    os.makedirs(output_dir, exist_ok=True)
    output_md = os.path.join(output_dir, filename)
    
    book_name_no_ext = filename.replace(".md", "")
    images_dir = os.path.join(output_dir, "images", book_name_no_ext)
    os.makedirs(images_dir, exist_ok=True)
    
    doc = fitz.open(pdf_path)
    total_pages = len(doc)
    print("🔍 Сканування PDF на наявність водяних знаків та фонів...")
    ignore_xrefs = get_frequent_xrefs(doc)
    if ignore_xrefs:
        print(f"🛡️ Знайдено та відфільтровано {len(ignore_xrefs)} повторюваних фонових елементів.")
    doc.close()
    
    page_queue = queue.Queue()
    for i in range(total_pages):
        page_queue.put(i)
        
    results_dict = {}
    failed_list = []
    progress_bar = tqdm(total=total_pages, desc="Парсинг сторінок")
    
    threads = []
    active_threads = {i: True for i in range(len(keys))}
    
    for idx, key in enumerate(keys):
        t = threading.Thread(target=worker_thread, args=(
            key, idx, page_queue, results_dict, failed_list, 
            pdf_path, images_dir, book_name_no_ext, progress_bar, db, active_threads, ignore_xrefs
        ))
        t.start()
        threads.append(t)
        time.sleep(0.1) # Майже миттєвий запуск, економимо секунди!
        
    while not page_queue.empty() and any(active_threads.values()):
        time.sleep(1)
        
    if not page_queue.empty() and not any(active_threads.values()):
        print("\n💀 КРИТИЧНА ПОМИЛКА: Всі ключі мертві або вичерпали ліміт! Збереження...")
        while not page_queue.empty():
            p = page_queue.get()
            results_dict[p] = f"\n\n> [!ERROR] [MISSING_PAGE_{p+1}_ALL_KEYS_DEAD]\n\n"
            failed_list.append(p+1)
            progress_bar.update(1)
            
    for t in threads:
        t.join(timeout=2)
        
    progress_bar.close()
    
    total_time = time.time() - start_time
    print(f"\n📝 Записуємо результати у файл у правильному порядку...")
    with open(output_md, "w", encoding="utf-8") as f:
        f.write(f"# {os.path.basename(pdf_path)}\n\n")
        for i in range(total_pages):
            if i in results_dict and results_dict[i]:
                f.write(results_dict[i] + "\n\n")
                
    print(f"🎉 Готово! Результат збережено у {output_md}")
    print(f"⏱️ Загальний час обробки: {total_time:.1f} сек")
    
    if failed_list:
        failed_list.sort()
        print("\n" + "="*60)
        print("⚠️ УВАГА! Наступні сторінки відхилені або не розпізнані:")
        print(", ".join(map(str, failed_list)))
        print("="*60 + "\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Швидкий парсер PDF у Markdown")
    parser.add_argument("input_pdf", help="Шлях до вхідного PDF файлу (обов'язково)")
    parser.add_argument("-o", "--output-dir", default=DEFAULT_OUTPUT_DIR, help="Папка для збереження Markdown")
    parser.add_argument("--keys", nargs="+", default=[], help="Кілька Gemini API ключів через пробіл")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input_pdf):
        print(f"❌ Вхідний файл не знайдено: {args.input_pdf}")
        sys.exit(1)
        
    final_keys = args.keys
    if not final_keys:
        env_keys = os.environ.get("GEMINI_API_KEYS")
        if env_keys:
            final_keys = [k.strip() for k in env_keys.split(",") if k.strip()]
            
    if not final_keys:
        print("❌ ПОМИЛКА: Не вказано жодного API-ключа!")
        sys.exit(1)
        
    unique_keys = list(set(final_keys))
    process_pdf(args.input_pdf, args.output_dir, unique_keys)
