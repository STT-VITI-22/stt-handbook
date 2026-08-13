# QA Dataset & Documentation Parsers

A toolkit for converting technical documentation, books, presentations, and web resources into Markdown format.

## Architecture

The project has a modular structure, split between local file parsers (PDF, PPTX) and web resource scrapers.

### 1. Document Parser (`tools/doc_parser/`)
Uses a combination of `PyMuPDF` for content extraction and the `Gemini API` for text formatting.

- **PPTX Mode (`--type pptx`)**: Extracts text and images from slides. Removes duplicated background images (watermarks) by comparing their MD5 hashes and areas. Slides are grouped by titles (`SlideChunker`) to avoid breaking sentences.
  - *Current flaws*: Title detection relies entirely on font size heuristics. This frequently fails if a slide contains larger incidental text (like a diagram number) or lacks a clear visual hierarchy.

- **PDF Mode (`--type pdf`)**: Designed for technical books. Uses `get_text("dict")` to extract rendered blocks. Features an OCR fallback if raw text is missing (scanned books).
  - *Current flaws*: The attempt to implement semantic chunking failed. To avoid API token limits, a hard limit of 5 pages per request was introduced, which reintroduces the problem of sentences being cut in half between chunks. The `dict` block analysis frequently scrambles the reading order (especially in multi-column layouts) and misses non-raster diagrams. Development on this parser is paused, and `legacy/gemini_pdf_parser.py` is temporarily used for books instead.

**Usage:**
```bash
# Parse a presentation
uv run python tools/doc_parser/parse_docs.py "path/to/lecture.pdf" --type pptx_doc

# Parse a book
uv run python tools/doc_parser/parse_docs.py "path/to/book.pdf" --type pdf
```

### 2. Web Scrapers (`tools/web_scrapers/`)
Parsers for web sources (executed via `tools/main.py <resource>`):
- **`gitbook`**: Parser for QA Bible. Instead of HTML scraping, it fetches `llms.txt` to get the sitemap and uses native `.md` endpoints to directly download raw Markdown. Image paths are converted to absolute URLs.
- **`qalight`**: Parses the QALight knowledge base via BeautifulSoup HTML analysis.
- **`dou`**: Parses dou.ua forum posts, stripping comments and UI elements.

### 3. Legacy Scripts (`tools/legacy/`)
Contains older monolithic parsers (e.g., `gemini_pdf_parser.py`, `gemini_pptx_parser.py`) that rely on strict page-by-page extraction.

## Dataset Output Structure

- `dataset/pptx_doc/` — Formatted technical presentations.
- `dataset/books_pdf/` — Converted IT literature (currently using the legacy parser).
- `dataset/QA_Bible/` — QA Bible knowledge base (GitBook).
- `dataset/qalight/`, `dataset/dou/` — Web-scraped articles.
