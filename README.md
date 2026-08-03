# QA Dataset ETL Pipeline

This repository contains an Extract-Transform-Load (ETL) pipeline for scraping, classifying, and formatting QA engineering articles into a structured dataset. Classification is performed via the Gemini API using Pydantic structured outputs to map content to ISTQB Foundation Level domains.

## Architecture

The pipeline is coordinated by `tools/main.py` and consists of three sequential phases:

### 1. Discovery (`etl/discovery.py`)
Fetches configured target URLs from `sources.yaml` and extracts article links via asynchronous HTTP requests (`httpx`) and CSS selector parsing (`BeautifulSoup`). Outputs to `raw_discovery.jsonl`.

### 2. Classification (`etl/ai.py`)
Evaluates discovered articles and assigns categories based on the ISTQB syllabus.
- **Content Analysis**: Fetches a 500-character content snippet for each URL before submitting the prompt, reducing classification errors caused by ambiguous titles.
- **Categorization**: Uses Gemini's structured output to assign a strict ISTQB domain (e.g., `test_levels`, `defect_management`). Irrelevant content is marked for deletion (`keep: False`).
- **Course Routing**: Articles containing `/kursy/` in their URL are forcefully overridden to the `courses` category via application logic, bypassing LLM classification.
Outputs to `manifest.jsonl`.

### 3. Download & Formatting (`etl/downloader.py`)
Downloads and converts the approved HTML articles to Markdown.
- **Idempotency**: The target `data/` directory is cleared prior to execution to prevent stale files from persisting.
- **Markdown Conversion**: Uses `markdownify`. Inline images nested within headings or structural tags are preserved via `keep_inline_images_in`. Escapes literal HTML tags (e.g., `<head>`) into code blocks to prevent Markdown rendering issues.

## Usage

Set the required environment variable:
```bash
export GEMINI_API_KEY="your_api_key_here"
```

Execute the full pipeline:
```bash
uv run python tools/main.py run_all --strategy topic
```

### Strategies
- `--strategy topic` (default): Uses the LLM-assigned ISTQB domains for the output directory structure.
- `--strategy source`: Uses the original hierarchical paths from the source website. Note that `/kursy/` URLs are still isolated into the `courses/` directory.

## Configuration
Sources and scraping parameters are defined in `tools/sources.yaml`.
