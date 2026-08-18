# Інструкція з використання парсерів статей (`web_scrapers`)

Цей набір скриптів призначений для автоматизованого збору статей та їхньої конвертації у формат Markdown. Скрипти автоматично очищують HTML від маркетингових блоків, коментарів та відновлюють посилання на зображення.

---

## 1. `fetch_articles.py` — Універсальний парсер (DOU, AgileLaws тощо)

Скрипт завантажує сторінку за вказаним URL, витягує основний текстовий контент та зберігає його у файл `.md`.

### Синтаксис:
```bash
python3 tools/web_scrapers/fetch_articles.py <URL> <ШЛЯХ_ДЛЯ_ЗБЕРЕЖЕННЯ.md> [--type dou]
```

### Приклади використання:

**Для стандартних ресурсів (наприклад, AgileLaws, Prometheus):**
```bash
python3 tools/web_scrapers/fetch_articles.py "https://agilelaws.com/..." "dataset/articles/agilelaws/my_article.md"
```

**Для статей на DOU (з відсіканням секцій коментарів):**
```bash
python3 tools/web_scrapers/fetch_articles.py "https://dou.ua/..." "dataset/articles/dou/new_article.md" --type dou
```

---

## 2. `parse_medium_html.py` — Спеціалізований парсер для Medium

Сайт Medium часто блокує автоматичні запити (помилка 403). Тому для обробки цих статей використовується локальний парсер, який працює з попередньо завантаженими HTML-файлами. 

Цей скрипт відновлює коректні посилання на зображення (обхід lazy-loading через тег `<noscript>`) та видаляє допоміжні блоки (профілі авторів, час читання, кнопки поширення).

### Порядок дій:

1. Відкрийте потрібну статтю на Medium у веб-браузері.
2. Збережіть сторінку на комп'ютер у форматі `HTML Only` (Тільки HTML).
3. Запустіть скрипт, вказавши шлях до збереженого файлу та шлях для нового markdown-документа:

```bash
python3 tools/web_scrapers/parse_medium_html.py <ШЛЯХ_ДО_HTML_ФАЙЛУ> <ШЛЯХ_ДЛЯ_ЗБЕРЕЖЕННЯ.md>
```

### Приклад:
```bash
python3 tools/web_scrapers/parse_medium_html.py "/Downloads/Medium_Article.html" "dataset/articles/medium/cool_article.md"
```

---

## Залежності

Для роботи скриптів необхідні зовнішні бібліотеки. Встановлення за допомогою `uv`:

```bash
uv pip install beautifulsoup4 markdownify requests
```
