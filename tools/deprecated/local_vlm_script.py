!pip install -q transformers accelerate qwen-vl-utils torchvision

import fitz
import torch
from transformers import Qwen2VLForConditionalGeneration, AutoProcessor
from qwen_vl_utils import process_vision_info
from PIL import Image
import io

print("Завантаження локальної Vision-моделі (Qwen2-VL-2B) у пам'ять GPU...")
model = Qwen2VLForConditionalGeneration.from_pretrained(
    "Qwen/Qwen2-VL-2B-Instruct",
    torch_dtype=torch.float16,
    device_map="cuda"
)
processor = AutoProcessor.from_pretrained("Qwen/Qwen2-VL-2B-Instruct")

pdf_path = "testyvan.pdf"
output_md = "testyvan_local_vlm.md"
doc = fitz.open(pdf_path)

print(f"Починаємо обробку {len(doc)} сторінок через ЛОКАЛЬНУ модель...")

with open(output_md, "w", encoding="utf-8") as f:
    f.write("# Розпізнаний підручник (Local VLM)\n\n")

for page_num in range(len(doc)):
    print(f"\n--- Сторінка {page_num + 1} / {len(doc)} ---")
    page = doc[page_num]
    pix = page.get_pixmap(dpi=150)
    img = Image.open(io.BytesIO(pix.tobytes("png")))
    
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "image", "image": img},
                {"type": "text", "text": "Витягни весь текст з цього зображення у форматі Markdown. Збережи всі заголовки. Обгорни програмний код у блок ```cpp ... ```. Формули відтворюй за допомогою Markdown/LaTeX. Поверни ТІЛЬКИ витягнутий Markdown текст."}
            ]
        }
    ]
    
    text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    image_inputs, video_inputs = process_vision_info(messages)
    inputs = processor(
        text=[text],
        images=image_inputs,
        videos=video_inputs,
        padding=True,
        return_tensors="pt"
    ).to("cuda")
    
    generated_ids = model.generate(**inputs, max_new_tokens=2048)
    generated_ids_trimmed = [
        out_ids[len(in_ids):] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
    ]
    output_text = processor.batch_decode(generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
    
    with open(output_md, "a", encoding="utf-8") as f:
        f.write(f"\n\n<!-- PAGE_{page_num + 1} -->\n\n" + output_text)
        
print("\nГотово! Книга збережена локально без жодних API лімітів.")
