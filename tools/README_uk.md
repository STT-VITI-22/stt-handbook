# Набір інструментів парсингу (QA Dataset Tools)

Ця директорія містить скрипти для конвертації навчальних матеріалів (презентацій, книг, статей, відео) у формат Markdown для датасету.

## Структура директорій

### 1. `document_parsers/` (Робота з PDF та PPTX)
Інструменти для витягування тексту та зображень із бінарних файлів за допомогою PyMuPDF та генерації тексту через Gemini API. 

- **`popeliuha_pdf_parser.py`**: Монолітний парсер PDF-файлів (згенерованих із презентацій). Витягує вбудовані растрові зображення, фільтрує їх за MD5-хешем (для видалення фонів) і використовує Gemini API для формування тексту. Має ліміт 1 запит на 4.1 сек для уникнення помилок 429 та відключає API-ключі при вичерпанні ліміту `generate_content_free_tier_requests`.
- **`gemini_pptx_parser.py`**: Попередній варіант парсера презентацій, що використовувався для обробки директорії `lectures_pz_hz_rpnd`.
- **`doc_parser/` (підпапка)**: Модульний фреймворк для розширеного парсингу з класами для чанкінгу тексту.

**Приклад використання:**
```bash
# Встановити ключі середовища (розділені комою)
export GEMINI_API_KEYS="key1,key2,key3"

# Запустити парсер для файлів Popeliuha
uv run python tools/document_parsers/popeliuha_pdf_parser.py
```

### 2. `web_scrapers/` (Парсинг веб-сторінок)
Скрипти для витягування текстових статей із сайтів за допомогою BeautifulSoup.

- **`run_web_parsers.py`**: Головний файл запуску. Викликає підмодулі (`dou.py`, `qalight.py`, `gitbook.py`) для збору контенту та видалення навігаційних елементів.

**Приклад використання:**
```bash
uv run python tools/web_scrapers/run_web_parsers.py qalight
uv run python tools/web_scrapers/run_web_parsers.py dou
```

### 3. `youtube_processors/` (Робота з аудіо та субтитрами)
Інструменти для завантаження контенту з YouTube та його транскрипції.

- **`fetch_popeliuha.py`**: Завантажує субтитри (VTT) та аудіо (.m4a) за вказаними посиланнями.
- **`whisper_transcribe.py`**: Локально транскрибує аудіофайли у текст за допомогою моделі OpenAI Whisper. Використовується для відео без вбудованих субтитрів.
- **`cleanup_popeliuha.py`**: Очищає VTT-файли від часових міток.

**Приклад використання:**
```bash
uv run python tools/youtube_processors/whisper_transcribe.py --input "dataset/youtube/audio/lecture.m4a"
```

### 4. `qa_and_formatters/` (Перевірка Markdown)
Скрипти для перевірки згенерованих файлів на синтаксичні помилки.

- **`check_broken_code.py` / `merge_code_blocks.py`**: Знаходить і об'єднує розірвані блоки коду (```), що виникають при чанкінгу.
- **`check_broken_links.py`**: Перевіряє наявність локальних зображень, на які є посилання в текстах.

**Приклад використання:**
```bash
uv run python tools/qa_and_formatters/check_broken_code.py --dir "dataset/articles"
```

### 5. `dataset_utils/` (Допоміжні інструменти)
Утиліти для метаданих та API-ключів.

- **`extract_popeliuha_links.py`**: Розпаковує `.xlsx` файли як архіви, витягує гіперпосилання на Google Slides із `sharedStrings.xml` та `sheet1.xml.rels`, і формує прямі посилання на завантаження.
- **`test_keys.py`**: Перевіряє масив ключів Gemini API на залишок квоти.

**Приклад використання:**
```bash
uv run python tools/dataset_utils/test_keys.py
```

### 6. `deprecated/` (Застарілі інструменти)
Містить скрипти, які виявилися неробочими або застарілими. Сюди належать експерименти з `marker-pdf` (спричиняв OOM і вимагав llama.cpp), `MinerU`, `Docling` та налаштування для хмарних середовищ (Colab).
