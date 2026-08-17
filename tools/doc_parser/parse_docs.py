import os
import sys
import argparse
import time
import glob
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

from core.gemini_client import GeminiClient
from core.chunker import SlideChunker
from extractors.pptx_extractor import PPTXExtractor
from generators.llm_generator import LLMGenerator

def parse_keys(args_keys: list) -> list:
    keys = []
    for k_group in args_keys:
        keys.extend([k.strip().strip('"').strip("'") for k in k_group.split(",") if k.strip()])
    if not keys:
        env_keys = os.environ.get("GEMINI_API_KEYS")
        if env_keys:
            keys = [k.strip().strip('"').strip("'") for k in env_keys.split(",") if k.strip()]
    return list(set(keys))

from slugify import slugify

def get_smart_filename(client: GeminiClient, slides, original_name: str) -> str:
    """
    Генерує безпечну транслітеровану назву файлу на базі оригінальної назви.
    (Відключено генерацію через LLM, оскільки вона призводила до викривлення типів занять, напр. lecture замість ГЗ).
    """
    clean_name = original_name.replace(".pdf", "").replace(".pptx", "")
    safe_name = slugify(clean_name, separator="_")
    return safe_name

def process_pptx(pdf_path: str, output_dir: str, client: GeminiClient):
    print(f"\n============================================================")
    print(f"Обробляємо PPTX: {pdf_path}")
    
    book_name_ext = os.path.basename(pdf_path)
    book_name_no_ext = book_name_ext.replace(".pdf", "").replace(".pptx", "")
    
    # Тимчасова папка на базі сирого імені
    temp_slug = slugify(book_name_no_ext, separator="_") or f"doc_{int(time.time())}"
    temp_images_dir = os.path.join(output_dir, "images", temp_slug)
    
    # 1. Екстракція (витягуємо слайди, ігноруємо водяні знаки)
    print("🔍 Етап 1/3: Екстракція слайдів та зображень...")
    extractor = PPTXExtractor(pdf_path, temp_images_dir)
    slides = extractor.extract_slides()
    print(f"✅ Витягнуто {len(slides)} слайдів.")
    
    # Розумна назва (після того, як маємо текст слайдів)
    safe_book_name = get_smart_filename(client, slides, book_name_ext)
    print(f"✨ Фінальна назва файлу: {safe_book_name}.md")
    
    # Оновлюємо шляхи з новою назвою
    images_dir = os.path.join(output_dir, "images", safe_book_name)
    md_file_path = os.path.join(output_dir, f"{safe_book_name}.md")
    
    # Перейменовуємо папку з картинками, яку вже створив екстрактор
    old_images_dir = extractor.images_dir
    if old_images_dir != images_dir and os.path.exists(old_images_dir):
        os.rename(old_images_dir, images_dir)
        # Оновлюємо шляхи в об'єктах ImageMeta
        for slide in slides:
            for img in slide.images:
                img.path = img.path.replace(old_images_dir, images_dir)
    
    # 2. Семантичне групування (склеюємо слайди за заголовками)
    print("\n🧠 Етап 2/3: Семантичне групування контексту...")
    chunks = SlideChunker.chunk_slides(slides)
    print(f"✅ Сформовано {len(chunks)} логічних розділів (Chunks). Деталі:")
    
    for i, chunk in enumerate(chunks):
        slide_nums = [str(p.page_num + 1) for p in chunk.pages]
        img_count = len(chunk.all_images)
        title_disp = chunk.title if chunk.title else "[Без заголовка]"
        print(f"   🔹 Розділ {i+1}: «{title_disp}» (Слайди: {', '.join(slide_nums)}) -> Картинки: {img_count}")
    
    # 3. Генерація через LLM (багатопотоково)
    print("\n🚀 Етап 3/3: Генерація Markdown (Gemini)...")
    generator = LLMGenerator(client, safe_book_name)
    
    results = [None] * len(chunks)
    
    # Використовуємо строго 1 потік на 1 ключ, щоб уникнути 429 та 503 помилок від Gemini
    workers = max(1, len(client.pool.keys))
    print(f"⚙️ Запущено {workers} потоків (відповідно до кількості ключів).")
    
    with ThreadPoolExecutor(max_workers=workers) as executor:
        # Створюємо мапу майбутніх задач
        future_to_idx = {}
        for i, chunk in enumerate(chunks):
            # Додаємо мікрозатримку між запусками потоків, щоб не було миттєвого сплеску (burst)
            time.sleep(0.5)
            future = executor.submit(generator.generate_markdown, chunk)
            future_to_idx[future] = i
        
        with tqdm(total=len(chunks), desc="Парсинг розділів") as pbar:
            for future in as_completed(future_to_idx):
                idx = future_to_idx[future]
                try:
                    md_text = future.result()
                    results[idx] = md_text
                except Exception as e:
                    results[idx] = f"\n\n> [!ERROR] Помилка генерації розділу: {e}\n\n"
                pbar.update(1)
                
    # 4. Запис результату
    print("📝 Запис результатів...")
    with open(md_file_path, "w", encoding="utf-8") as f:
        f.write(f"# {book_name_no_ext}\n\n")
        for chunk_md in results:
            if chunk_md:
                f.write(chunk_md + "\n\n")
                
    print(f"🎉 Готово! Файл збережено: {md_file_path}")
    
    # 5. Очищення тимчасових картинок контексту
    print("🧹 Очищення тимчасових файлів...")
    full_images = glob.glob(os.path.join(images_dir, "*_full.jpeg"))
    for f in full_images:
        try:
            os.remove(f)
        except Exception as e:
            pass
    if full_images:
        print(f"🗑️ Видалено {len(full_images)} тимчасових зображень слайдів.")


from extractors.pdf_extractor import PDFExtractor

def process_pdf(pdf_path: str, output_dir: str, client: GeminiClient):
    print(f"\n============================================================")
    print(f"Обробляємо PDF: {pdf_path}")
    
    book_name_ext = os.path.basename(pdf_path)
    book_name_no_ext = book_name_ext.replace(".pdf", "")
    
    # Розумна назва 
    safe_book_name = get_smart_filename(client, [], book_name_ext)
    print(f"✨ Фінальна назва файлу: {safe_book_name}.md")
    
    images_dir = os.path.join(output_dir, "images", safe_book_name)
    md_file_path = os.path.join(output_dir, f"{safe_book_name}.md")
    
    # 1. Екстракція 
    print("🔍 Етап 1/3: Екстракція сторінок та зображень...")
    extractor = PDFExtractor(pdf_path, images_dir)
    slides = extractor.extract_slides()
    print(f"✅ Витягнуто {len(slides)} сторінок.")
    
    # 2. Семантичне групування (склеюємо слайди за заголовками)
    print("\n🧠 Етап 2/3: Семантичне групування контексту...")
    chunks = SlideChunker.chunk_slides(slides)
    print(f"✅ Сформовано {len(chunks)} логічних розділів (Chunks). Деталі:")
    
    for i, chunk in enumerate(chunks):
        slide_nums = [str(p.page_num + 1) for p in chunk.pages]
        img_count = len(chunk.all_images)
        title_disp = chunk.title if chunk.title else "[Без заголовка]"
        print(f"   🔹 Розділ {i+1}: «{title_disp}» (Сторінки: {', '.join(slide_nums)}) -> Картинки: {img_count}")
    
    # 3. Генерація через LLM (багатопотоково)
    print("\n🚀 Етап 3/3: Генерація Markdown (Gemini)...")
    generator = LLMGenerator(client, safe_book_name)
    
    results = [None] * len(chunks)
    workers = max(1, len(client.pool.keys))
    print(f"⚙️ Запущено {workers} потоків (відповідно до кількості ключів).")
    
    with ThreadPoolExecutor(max_workers=workers) as executor:
        future_to_idx = {}
        for i, chunk in enumerate(chunks):
            time.sleep(0.5)
            future = executor.submit(generator.generate_markdown, chunk)
            future_to_idx[future] = i
        
        with tqdm(total=len(chunks), desc="Парсинг розділів") as pbar:
            for future in as_completed(future_to_idx):
                idx = future_to_idx[future]
                try:
                    md_text = future.result()
                    results[idx] = md_text
                except Exception as e:
                    results[idx] = f"\n\n> [!ERROR] Помилка генерації розділу: {e}\n\n"
                pbar.update(1)
                
    # 4. Запис результату
    print("📝 Запис результатів...")
    with open(md_file_path, "w", encoding="utf-8") as f:
        f.write(f"# {book_name_no_ext}\n\n")
        for chunk_md in results:
            if chunk_md:
                f.write(chunk_md + "\n\n")
                
    print(f"🎉 Готово! Файл збережено: {md_file_path}")
    
    # 5. Очищення тимчасових картинок контексту
    print("🧹 Очищення тимчасових файлів...")
    full_images = glob.glob(os.path.join(images_dir, "*_full.jpeg"))
    for f in full_images:
        try:
            os.remove(f)
        except Exception as e:
            pass
    if full_images:
        print(f"🗑️ Видалено {len(full_images)} тимчасових зображень сторінок.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Модульний парсер документів (PDF/PPTX)")
    parser.add_argument("input_path", help="Шлях до файлу (наприклад, Лекція.pdf)")
    parser.add_argument("--type", choices=["pptx", "pdf", "web"], required=True, help="Тип документа")
    parser.add_argument("-o", "--output-dir", default=None, help="Папка для результатів (за замовчуванням dataset/{type}/parsed)")
    parser.add_argument("--keys", nargs="+", default=[], help="Gemini API ключі")
    
    args = parser.parse_args()
    
    # Перевірка входу
    if not os.path.exists(args.input_path):
        print(f"❌ Файл не знайдено: {args.input_path}")
        sys.exit(1)
        
    keys = parse_keys(args.keys)
    if not keys:
        print("❌ Не вказано жодного API ключа!")
        sys.exit(1)
        
    # Формування стандартної структури (Нормальної)
    if args.output_dir is None:
        type_dir = "books_pdf" if args.type == "pdf" else args.type
        args.output_dir = f"dataset/{type_dir}/parsed"
        
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Ініціалізація єдиного клієнта на весь запуск
    client = GeminiClient(keys)
    
    # Роутінг за типом
    if args.type == "pptx":
        process_pptx(args.input_path, args.output_dir, client)
    elif args.type == "pdf":
        process_pdf(args.input_path, args.output_dir, client)
    elif args.type == "web":
        print("🛠️ Web Extractor ще в розробці.")
