import os
import subprocess
import sys

print("🚀 Встановлюємо правильні (старі й робочі) версії Marker та Surya-OCR...")
subprocess.run([sys.executable, "-m", "pip", "install", "uv"], check=True)
subprocess.run([
    sys.executable, "-m", "uv", "pip", "install", "--system", "--reinstall",
    "marker-pdf==0.2.8", "surya-ocr==0.4.14", "transformers==4.41.2", "torchvision"
], check=True)

print("🧹 Прибираємо сліди старого зламаного патчу (якщо вони лишилися)...")
import site
for p in site.getsitepackages():
    decoder_path = os.path.join(p, "surya", "model", "ordering", "decoder.py")
    if os.path.exists(decoder_path):
        with open(decoder_path, "r") as f:
            content = f.read()
        if "'sdpa': MBartAttention," in content:
            content = content.replace("\n    'sdpa': MBartAttention,", "")
            with open(decoder_path, "w") as f:
                f.write(content)
            print("✅ Старий патч успішно видалено з decoder.py!")

print("🩹 Застосовуємо правильний патч для сумісності з новими transformers (eager fix)...")
surya_path = None
for p in site.getsitepackages():
    candidate = os.path.join(p, "surya", "model", "ordering", "model.py")
    if os.path.exists(candidate):
        surya_path = candidate
        break

if surya_path:
    with open(surya_path, "r") as f:
        content = f.read()
    
    if "config._attn_implementation" not in content:
        content = content.replace(
            "model = OrderVisionEncoderDecoderModel.from_pretrained",
            "config._attn_implementation = 'eager'\n    model = OrderVisionEncoderDecoderModel.from_pretrained"
        )
        with open(surya_path, "w") as f:
            f.write(content)
        print("✅ Патч (eager) успішно застосовано!")
    else:
        print("⚠️ Патч не застосовано (можливо, він вже є або структура файлу інша).")
else:
    print("⚠️ Не вдалося знайти файл surya для патчингу.")

print("🩹 Застосовуємо патч для pdftext (fix TypeError: PdfDocument)...")
for p in site.getsitepackages():
    candidate = os.path.join(p, "pdftext", "extraction.py")
    if os.path.exists(candidate):
        with open(candidate, "r") as f:
            content = f.read()
        if "PdfDocument': return pdf" not in content:
            content = content.replace(
                "pdf = pdfium.PdfDocument(pdf)",
                "if type(pdf).__name__ == 'PdfDocument': return pdf\n    pdf = pdfium.PdfDocument(pdf)"
            )
            with open(candidate, "w") as f:
                f.write(content)
            print("✅ Патч pdftext успішно застосовано!")
        break

print("🩹 Застосовуємо патч для marker (fix closed PdfDocument pointer)...")
for p in site.getsitepackages():
    candidate = os.path.join(p, "marker", "convert.py")
    if os.path.exists(candidate):
        with open(candidate, "r") as f:
            content = f.read()
        if "doc = pdfium.PdfDocument(fname)\n    surya_detection" not in content:
            content = content.replace(
                "surya_detection(doc, pages,",
                "doc = pdfium.PdfDocument(fname)\n    surya_detection(doc, pages,"
            )
            with open(candidate, "w") as f:
                f.write(content)
            print("✅ Патч marker convert успішно застосовано!")
        break

INPUT_PDF = "testyvan.pdf"
OUTPUT_DIR = "./output"

if not os.path.exists(INPUT_PDF):
    print(f"❌ ПОМИЛКА: Файл {INPUT_PDF} не знайдено у середовищі Colab! Завантажте його.")
else:
    print(f"🔄 Починаємо конвертацію {INPUT_PDF}...")
    import shlex
    env = os.environ.copy()
    # Зменшуємо max_pages до 20, бо Colab має ліміт оперативної пам'яті (12 ГБ).
    # Якщо завантажити 500 сторінок у пам'ять як картинки, ядро Colab просто крашнеться (OOM) без помилок.
    cmd = ["marker_single", INPUT_PDF, OUTPUT_DIR, "--max_pages", "20"]
    print(f"🚀 Виконуємо команду: {' '.join(shlex.quote(arg) for arg in cmd)}")
    
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    error_log = []
    
    for line in process.stdout:
        print(line, end="")
        error_log.append(line)
        
    process.wait()
    
    if process.returncode == 0:
        print("\n🎉 === УСПІШНО ГОТОВО! === 🎉")
        print(f"📄 Результат шукайте в папці {OUTPUT_DIR} (зліва у файлах).")
    else:
        print(f"\n❌ СТАЛАСЯ ПОМИЛКА! Marker впав із кодом {process.returncode}.")
        if error_log:
            print("\n--- ОСТАННІ РЯДКИ ЛОГУ ---")
            print("".join(error_log[-30:]))
