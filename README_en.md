# QA Knowledge Base Dataset (By-Source Branch)

This repository contains a dataset of materials for QA engineers, as well as an ETL pipeline for its population.

## Dataset Structure

This branch implements source-based organization. Data is stored in exact accordance with the hierarchy of its original source (e.g., the navigation menu of a website). This approach preserves the context and intent of the authors.
*An alternative branch `dataset/by-topic` contains the same data, but reorganized into domain categories (e.g., ISTQB).*

Current structure:
- `data/` (or folders named by domains, e.g., `qalight.ua/`)
  - `automation-of-testing/`
  - `databases/`
  - ...and other original sections of the site.

## Collection Tool (`tools/pipeline.py`)

A custom ETL script is used for automated collection, operating in three stages:
1. **Discover:** Asynchronous parsing of the site's navigation menu (multi-level lists) to form path structures like `domain/category/subcategory` and save them in `raw_discovery.jsonl`.
2. **Classify:** LLM analysis (Gemini API) via `google-genai` and `pydantic`. The model acts solely as a filter (`keep: True/False`), discarding irrelevant general IT articles. A sliding window algorithm prevents API blocking (limit of 5 requests/min) during batch processing of 30 articles.
3. **Download:** Asynchronous downloading (`httpx`), HTML cleaning (`BeautifulSoup4`), and saving in Markdown (`markdownify`) while preserving the generated folder structure.

### Dependencies and Usage
The classification stage requires an environment variable:
`export GEMINI_API_KEY="your_key"`

Run the pipeline:
```bash
python tools/pipeline.py -h
```

## Next Steps
- Parsing PDF (PyMuPDF) and DOCX (python-docx). Data from these sources will be placed in separate folders named after their authors or sources.
