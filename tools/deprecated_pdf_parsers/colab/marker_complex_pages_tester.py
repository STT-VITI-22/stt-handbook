!pip install pypdf -q
from pypdf import PdfReader, PdfWriter
import subprocess
import shlex

# 1. Вирізаємо найскладніші сторінки (наприклад, 112-135, де йдуть графи і код)
reader = PdfReader("testyvan.pdf")
writer = PdfWriter()

# Сторінки нумеруються з 0, тому беремо діапазон [111:135]
for i in range(111, min(135, len(reader.pages))):
    writer.add_page(reader.pages[i])

with open("complex_pages.pdf", "wb") as f:
    writer.write(f)

print("✅ Вирізано складні сторінки у файл complex_pages.pdf")

# 2. Запускаємо Marker ТІЛЬКИ для цього складного шматка
cmd = ["marker_single", "complex_pages.pdf", "./output_complex", "--max_pages", "50"]
print(f"🚀 Запускаємо Marker для перевірки картинок і коду...")

process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
for line in process.stdout:
    print(line, end="")
process.wait()

if process.returncode == 0:
    print("\n🎉 ГОТОВО! Шукайте результат у папці ./output_complex/")
else:
    print(f"\n❌ СТАЛАСЯ ПОМИЛКА! Код: {process.returncode}")
