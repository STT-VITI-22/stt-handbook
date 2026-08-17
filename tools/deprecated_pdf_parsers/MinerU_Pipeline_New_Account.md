# Повний пайплайн для нового акаунта Colab (MinerU / Magic-PDF)

Оскільки ви будете на новому акаунті, вам потрібно буде завантажити ваші PDF-файли заново. Найкраще створити папку на Google Drive (наприклад, `MinerU_Input`) і покласти всі ваші PDF-файли туди, щоб обробляти їх масово.

Створіть новий блокнот у Colab, переконайтеся, що **ввімкнено T4 GPU** (Середовище виконання -> Змінити тип середовища виконання), і скопіюйте ці 3 комірки.

### Комірка 1: Встановлення бібліотек та підключення Диску
```python
from google.colab import drive
drive.mount('/content/drive')

print("Встановлення MinerU та залежностей...")
!pip install -q -U "magic-pdf[full]" --extra-index-url https://wheels.myhloli.com --trusted-host wheels.myhloli.com
!pip install -q huggingface_hub
!pip install -q 'git+https://github.com/facebookresearch/detectron2.git'
!python -c "f1='/usr/local/lib/python3.12/dist-packages/transformers/modeling_utils.py'; f2='/usr/local/lib/python3.12/dist-packages/transformers/pytorch_utils.py'; c='\ndef find_pruneable_heads_and_indices(*args, **kwargs): pass\ndef prune_linear_layer(*args, **kwargs): pass\n'; open(f1, 'a').write(c); open(f2, 'a').write(c)"

print("Встановлення завершено!")
```

### Комірка 2: Завантаження моделей, виправлення папок та створення конфігу
*Скопіюйте цей код кнопкою Copy, щоб не було відступів. Цей скрипт робить усю ту магію, до якої ми прийшли.*
```python
import os
import json

from huggingface_hub import snapshot_download
print("1. Завантаження моделей (качаємо ~10 ГБ, це займе кілька хвилин)...")
snapshot_download(repo_id="opendatalab/PDF-Extract-Kit", local_dir="/root/models")
snapshot_download(repo_id="opendatalab/PDF-Extract-Kit-1.0", allow_patterns=["models/OCR/*"], local_dir="/root/models")
snapshot_download(repo_id="juliozhao/DocLayout-YOLO-DocStructBench-imgsz1280-2501", local_dir="/root/models/models/Layout/YOLO")

print("2. Виправлення шляхів для сумісності з кодом...")
os.makedirs("/root/models/models/MFD/YOLO", exist_ok=True)
os.system("cp /root/models/models/MFD/weights.pt /root/models/models/MFD/YOLO/yolo_v8_ft.pt")
os.makedirs("/root/models/models/Layout/LayoutLMv3", exist_ok=True)
os.system("cp /root/models/models/Layout/model_final.pth /root/models/models/Layout/LayoutLMv3/model_final.pth")
os.system("ln -sf /root/models/models/MFR/unimernet_small /root/models/models/MFR/unimernet_hf_small_2503")
os.system("ln -sf /root/models/models/MFR/unimernet_small/pytorch_model.pth /root/models/models/MFR/unimernet_small/pytorch_model.bin")

# Патч для transformers (виправлення ImportError через видалені модулі у v4.39.3)
import transformers
with open(transformers.__path__[0] + '/pytorch_utils.py', 'a') as f:
    f.write('\n\nclass Conv1D:\n    pass\n')

# Вирішення проблеми FileNotFoundError для OCR моделі
# Файл ch_PP-OCRv3_det_infer.pth був видалений з репозиторію восени 2025 року. 
# Ми завантажимо en_PP-OCRv3_det_infer.pth (яка має ідентичну архітектуру) з історичного коміту та перейменуємо її.
print("4. Відновлення видаленої OCR моделі...")
import urllib.request
ocr_dir = "/root/models/models/OCR/paddleocr_torch"
os.makedirs(ocr_dir, exist_ok=True)
models_to_download = {
    "ch_PP-OCRv3_det_infer.pth": "https://huggingface.co/opendatalab/PDF-Extract-Kit-1.0/resolve/a4f6a8d29a4d96730f90ea174a9322e842b93552/models/OCR/paddleocr_torch/en_PP-OCRv3_det_infer.pth",
    "cyrillic_PP-OCRv3_rec_infer.pth": "https://huggingface.co/opendatalab/PDF-Extract-Kit-1.0/resolve/a4f6a8d29a4d96730f90ea174a9322e842b93552/models/OCR/paddleocr_torch/cyrillic_PP-OCRv3_rec_infer.pth"
}
for filename, url in models_to_download.items():
    dest = f"{ocr_dir}/{filename}"
    if not os.path.exists(dest):
        urllib.request.urlretrieve(url, dest)
        print(f"✅ OCR модель {filename} успішно завантажено!")
    else:
        print(f"✅ OCR модель {filename} вже існує.")

print("3. Створення конфігураційного файлу...")
config = {
    "models-dir": "/root/models/models",
    "device-mode": "cuda",
    "layout-config": {
        "model": "doclayout_yolo"
    },
    "ocr-config": {
        "enable": True
    },
    "formula-config": {
        "enable": False
    }
}

with open('/root/magic-pdf.json', 'w') as f:
    json.dump(config, f, indent=4)

print("✅ Налаштування завершено успішно!")
```

### Комірка 3: Запуск масового парсингу
*Перед запуском переконайтеся, що шлях до вхідної папки (`-p`) правильний і містить ваші PDF-файли. Усі оброблені результати будуть збережені у вихідну папку (`-o`).*
```bash
!/usr/local/bin/magic-pdf -p "/content/drive/MyDrive/MinerU_Input" -o "/content/drive/MyDrive/MinerU_Output" -m txt --lang uk
```
