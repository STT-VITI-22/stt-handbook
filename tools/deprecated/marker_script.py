!pip install -q marker-pdf==0.3.2

import os
import torch
from marker.convert import convert_single_pdf
from marker.models import load_all_models

os.environ["IN_A_DOCKER_CONTAINER"] = "False"
os.environ["TORCH_DEVICE"] = "cuda" if torch.cuda.is_available() else "cpu"

print("Завантаження моделей Surya та Marker...")
model_lst = load_all_models()

pdf_path = "testyvan.pdf"
output_md = "testyvan_marker.md"

print(f"Починаємо парсинг {pdf_path}...")
full_text, images, out_meta = convert_single_pdf(pdf_path, model_lst)

with open(output_md, "w", encoding="utf-8") as f:
    f.write(full_text)

print(f"Готово! Результат збережено у {output_md}")
