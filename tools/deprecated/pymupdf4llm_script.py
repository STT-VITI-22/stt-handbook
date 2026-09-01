!pip install -q pymupdf4llm

import pymupdf4llm

pdf_path = "testyvan.pdf"
output_md = "testyvan_local.md"

print(f"Починаємо парсинг {pdf_path} через PyMuPDF4LLM...")
md_text = pymupdf4llm.to_markdown(pdf_path)

with open(output_md, "w", encoding="utf-8") as f:
    f.write(md_text)

print(f"Готово! Результат збережено у {output_md}")
