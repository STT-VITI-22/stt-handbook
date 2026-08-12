%%bash
echo "Починаємо завантаження моделей. Це займе кілька хвилин..."
# Оновлено репозиторій: розробники перейменували його на PDF-Extract-Kit!
huggingface-cli download opendatalab/PDF-Extract-Kit --local-dir /root/models

echo "Створюємо правильний конфіг..."
echo "{\"models-dir\": \"/root/models/models\", \"device-mode\": \"cuda\"}" > /root/magic-pdf.json

echo "Конфіг записано. Можете парсити!"
