%%bash
echo "Завершуємо виправлення (останній крок)..."

cd /root/models/models/

# Виправляємо формули (MFD)
mkdir -p MFD/YOLO
cp MFD/weights.pt MFD/YOLO/yolo_v8_ft.pt

# Виправляємо макет (Layout)
mkdir -p Layout/LayoutLMv3
cp Layout/model_final.pth Layout/LayoutLMv3/model_final.pth

# Виправляємо розпізнавання формул (MFR)
ln -sf unimernet_small MFR/unimernet_hf_small_2503

# ВАЖЛИВО: Розробники також змінили розширення файлу моделі з .bin на .pth
# Бібліотека transformers шукає .bin, тому ми створимо такий "ярлик"
cd MFR/unimernet_small
ln -sf pytorch_model.pth pytorch_model.bin

echo "Все! Більше помилок з файлами бути не може."
