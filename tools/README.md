# QA Dataset & Documentation Parsers

A modular toolkit for parsing complex technical documentation, books, presentations, and web articles into clean, LLM-ready Markdown.

## Architecture

The project has evolved into a modular architecture, prioritizing semantic chunking and high-fidelity extraction of complex documents (like PDFs and PPTXs) using Gemini API, alongside traditional web scrapers.

### 1. Document Parser (`tools/doc_parser/`)
The primary engine for parsing local documents. It uses a combination of `PyMuPDF` for structural extraction and the `Gemini API` for intelligent Markdown formatting.

- **PPTX Mode (`--type pptx`)**: Extracts text and images from presentation slides. Intelligently filters out watermarks and repeating background graphics. Uses a `SlideChunker` to semantically group consecutive slides with the same title into single logical sections to avoid breaking sentences across pages.
- **PDF Mode (`--type pdf`)**: Designed for technical books. Uses PyMuPDF's block-level `dict` extraction to surgically pull out only rendered images (ignoring shadows/lines). Features a dynamic Fallback to OCR mode if the PDF is a scanned book lacking a text layer. It groups pages into chunks (max 5 pages) to prevent token exhaustion.

**Usage:**
```bash
# Parse a presentation
uv run python tools/doc_parser/parse_docs.py "path/to/lecture.pdf" --type pptx

# Parse a book (vector or scanned)
uv run python tools/doc_parser/parse_docs.py "path/to/book.pdf" --type pdf
```

### 2. Web Scrapers (`tools/web_scrapers/`)
Dedicated parsers for web sources. *(Note: Currently isolated in their own directory).*
- **`qalight`**: Parses the QALight knowledge base, filtering out promo content.
- **`dou`**: Parses `dou.ua` forum posts, stripping comments and UI elements.

### 3. Legacy Scripts (`tools/legacy/`)
Contains deprecated monolithic parsers (e.g., `gemini_pdf_parser.py`, `gemini_pptx_parser.py`) preserved for historical reference and edge-case testing.

## Dataset Structure

The extracted and formatted Markdown files are organized by source:
- `dataset/pptx/parsed/` — Formatted technical presentations.
- `dataset/books_pdf/parsed/` — Converted IT literature and QA books.
- `dataset/qalight/`, `dataset/dou/` — Web-scraped articles.
