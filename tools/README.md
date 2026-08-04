# QA Dataset & Modular Parsers

A QA engineering dataset and a toolkit for data collection, conversion, and formatting.

## Architecture

This project uses a modular architecture. Instead of a single universal scraper, a dedicated isolated parser is created for each data source to handle its specific structure and requirements. The entry point is `tools/main.py`.

### Parsers (`tools/parsers/`)
- **`qalight`**: A parser for the QALight knowledge base. It parses the DOM to reconstruct the original site hierarchy while skipping promotional material and courses.
- **`dou`**: A forum parser for `dou.ua`. It fetches specific QA forum discussions and strips away comments, ads, and author blocks, extracting the primary text content.
- **`pdf`**: A local file processor that uses `pymupdf4llm` to batch-convert PDF files into Markdown, preserving tables, lists, and headings.

All web parsers inherit from `BaseParser`, which provides HTML-to-Markdown conversion, retaining inline images and escaping literal HTML tags for rendering.

## Usage

Run the script specifying the target parser:

```bash
uv run python tools/main.py qalight
uv run python tools/main.py dou
uv run python tools/main.py pdf
```

## Dataset Structure

The output is categorized by source in the `dataset/` directory:
- `dataset/qalight/`: Categorized by the site's original navigational taxonomy.
- `dataset/dou/articles/`: Technical forum posts.
- `dataset/books_pdf/`: Markdown conversions of QA literature.
