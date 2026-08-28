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
import queue
import threading
import json
import hashlib
from datetime import date
import pymupdf as fitz
from PIL import Image
from google import genai
from google.genai import types
from tqdm import tqdm

DEFAULT_INPUT_DIR = "dataset/pptx_doc/popeliuha/raw"
DEFAULT_OUTPUT_DIR = "dataset/pptx_doc/popeliuha/parsed"
DELAY_SECONDS = 4.1 
DAILY_LIMIT = 1500
MODEL_NAME = "gemini-3.5-flash-lite"

PROMPT = """Ти - експерт з конвертації навчальних презентацій Сергія Попелюхи у сучасний Markdown.
Твоє завдання: витягти текст з цього слайду з максимальним збереженням структури конспекту.

1. Текст: Форматуй як зв'язний конспект.
2. КОЛОНТИТУЛИ ТА РЕКВІЗИТИ: Повністю ІГНОРУЙ номери слайдів, дату, імена автора ("Сергій Попелюха", "Popeliuha"), посилання на соцмережі, логотипи.
3. СЛАЙДИ-ПОДЯКИ: Якщо слайд містить ЛИШЕ подяку ("Дякую за перегляд"), прохання про підписку — ПОВНІСТЮ ІГНОРУЙ ЦЕЙ СЛАЙД, повертай лише порожній рядок.
4. Код: ОБОВ'ЯЗКОВО обгорни програмний код або приклади у блоки (```мова ... ```).
5. ДІАГРАМ ТА БЛОК-СХЕМИ: Якщо бачиш логічну блок-схему (наприклад, State Transition), згенеруй її у Mermaid.js (```mermaid ... ```).
6. ЗОБРАЖЕННЯ: Знизу в системному повідомленні тобі буде передано список шляхів до растрових картинок, які були знайдені на цьому слайді. Якщо картинка має зміст (скріншот, мем, графік) - обов'язково додай її в текст за вказаним шляхом `![Опис](шлях)`.
"""

class KeyUsageDB:
    def __init__(self, db_path):
        self.db_path = db_path
        self.lock = threading.Lock()
        self.usage = self._load()
    def _load(self):
        if os.path.exists(self.db_path):
            try:
                with open(self.db_path, "r", encoding="utf-8") as f: return json.load(f)
            except Exception: pass
        return {}
    def _save(self):
        with open(self.db_path, "w", encoding="utf-8") as f: json.dump(self.usage, f, indent=4)
    def mask_key(self, api_key):
        return api_key[:6] + "..." + api_key[-4:] if len(api_key) >= 12 else api_key
    def increment(self, api_key):
        today = str(date.today())
        masked = self.mask_key(api_key)
        with self.lock:
            if masked not in self.usage or self.usage[masked].get("date") != today:
                self.usage[masked] = {"date": today, "count": 0}
            self.usage[masked]["count"] += 1
            self._save()
            return self.usage[masked]["count"]

def get_frequent_image_hashes(doc, threshold=3):
    hash_counts = {}
    for i in range(len(doc)):
        for img in doc.load_page(i).get_images(full=True):
            base_image = doc.extract_image(img[0])
            if "image" in base_image:
                h = hashlib.md5(base_image["image"]).hexdigest()
                hash_counts[h] = hash_counts.get(h, 0) + 1
    return {h for h, count in hash_counts.items() if count > threshold}

def extract_raster_images(doc, page, page_num, images_dir, ignore_hashes):
    saved_images = []
    valid_images = []
    for img in page.get_images(full=True):
        base = doc.extract_image(img[0])
        if "image" not in base: continue
        if hashlib.md5(base["image"]).hexdigest() in ignore_hashes: continue
        if base.get("width", 0) < 100 or base.get("height", 0) < 100: continue
        valid_images.append(base)
        
    for i, base in enumerate(valid_images):
        name = f"page_{page_num}_img_{i+1}.{base['ext']}"
        with open(os.path.join(images_dir, name), "wb") as f: f.write(base["image"])
        saved_images.append(name)
    return saved_images

def worker_thread(api_key, key_index, page_queue, results_dict, failed_list, pdf_path, images_dir, book_name, progress_bar, db, active_threads, ignore_hashes):
    client = genai.Client(api_key=api_key)
    doc = fitz.open(pdf_path)
    last_req = 0
    masked = db.mask_key(api_key)
    
    while True:
        try:
            page_num = page_queue.get_nowait()
        except queue.Empty:
            break
            
        elapsed = time.time() - last_req
        if elapsed < DELAY_SECONDS:
            time.sleep(DELAY_SECONDS - elapsed)
            
        page = doc.load_page(page_num)
        saved = extract_raster_images(doc, page, page_num+1, images_dir, ignore_hashes)
        pix = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0))
        img_part = types.Part.from_bytes(data=pix.tobytes("jpeg"), mime_type="image/jpeg")
        
        d_prompt = PROMPT
        if saved:
            paths = [f"images/{book_name}/{img}" for img in saved]
            d_prompt += f"\n\n[СИСТЕМНЕ ПОВІДОМЛЕННЯ]: На цій сторінці знайдено {len(saved)} растрових зображень: {', '.join(paths)}. Якщо бачиш їх, обов'язково встав у текст посилання у форматі ![Опис](шлях)."
            
        success = False
        fatal_error = False
        for _ in range(3):
            last_req = time.time()
            try:
                resp = client.models.generate_content(model=MODEL_NAME, contents=[d_prompt, img_part])
                results_dict[page_num] = resp.text.strip() if resp.text else ""
                db.increment(api_key)
                progress_bar.update(1)
                success = True
                break
            except Exception as e:
                err = str(e).lower()
                if "429" in err and "generate_content_free_tier_requests" in err:
                    print(f"\n⚠️ Ключ {masked} вичерпав ліміт. Потік зупиняється.")
                    fatal_error = True
                    break
                elif "429" in err:
                    time.sleep(10)
                else:
                    time.sleep(2)
                    
        if fatal_error:
            page_queue.put(page_num)
            break
        
        if not success:
            page_queue.put(page_num)
            time.sleep(5)
            
    doc.close()
    active_threads[key_index] = False

def process_pdf(pdf_path, output_md, keys, db, base_images_dir):
    doc = fitz.open(pdf_path)
    total_pages = len(doc)
    ignore = get_frequent_image_hashes(doc, 3)
    doc.close()
    
    book_name = os.path.basename(pdf_path).replace(".pdf", "").replace(".pptx", "")
    img_dir = os.path.join(base_images_dir, book_name)
    os.makedirs(img_dir, exist_ok=True)
    
    q = queue.Queue()
    for i in range(total_pages): q.put(i)
    
    res = {}
    failed = []
    pbar = tqdm(total=total_pages, desc=book_name[:30], leave=False)
    
    threads = []
    active = {i: True for i in range(len(keys))}
    for i, k in enumerate(keys):
        t = threading.Thread(target=worker_thread, args=(k, i, q, res, failed, pdf_path, img_dir, book_name, pbar, db, active, ignore))
        t.start()
        threads.append(t)
        time.sleep(0.1)
        
    while any(active.values()): time.sleep(0.5)
    for t in threads: t.join()
    pbar.close()
    
    if not q.empty():
        print(f"❌ Не вдалося обробити {q.qsize()} сторінок (всі ключі вичерпано).")
        return False
        
    with open(output_md, "w", encoding="utf-8") as f:
        f.write(f"# {book_name}\n\n")
        for i in range(total_pages):
            if i in res and res[i].strip():
                f.write(res[i] + "\n\n")
    return True

if __name__ == "__main__":
    with open("local-dev/gemini_keys.txt", "r") as f: keys = [k.strip() for k in f.read().split(",") if k.strip()]
    if not keys: sys.exit(1)
    
    os.makedirs(DEFAULT_OUTPUT_DIR, exist_ok=True)
    img_dir = os.path.join(DEFAULT_OUTPUT_DIR, "images")
    os.makedirs(img_dir, exist_ok=True)
    db = KeyUsageDB(os.path.join(DEFAULT_OUTPUT_DIR, "api_usage.json"))
    
    files = sorted([f for f in os.listdir(DEFAULT_INPUT_DIR) if f.endswith('.pdf')])
    for f in files:
        in_p = os.path.join(DEFAULT_INPUT_DIR, f)
        out_p = os.path.join(DEFAULT_OUTPUT_DIR, f.replace(".pdf", ".md"))
        if not os.path.exists(out_p):
            success = process_pdf(in_p, out_p, keys, db, img_dir)
            if not success:
                print("🛑 Процес зупинено через вичерпання ключів.")
                break
