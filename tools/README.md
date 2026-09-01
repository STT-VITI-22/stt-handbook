# QA Dataset Tools

This directory contains scripts for converting educational materials (presentations, books, articles, videos) into Markdown format for the dataset.

## Directory Structure

### 1. `document_parsers/` (PDF & PPTX Parsing)
Tools for extracting text and images from binary files using PyMuPDF and generating text via the Gemini API.

- **`popeliuha_pdf_parser.py`**: A monolithic parser for PDFs generated from presentations. Extracts embedded raster images, filters them by MD5 hash (to ignore backgrounds), and uses the Gemini API to format text. Includes a 4.1-second delay per request to avoid 429 errors and disables keys upon exhausting the `generate_content_free_tier_requests` limit.
- **`gemini_pptx_parser.py`**: The previous presentation parser version, used for processing the `lectures_pz_hz_rpnd` directory.
- **`doc_parser/` (subfolder)**: A modular framework for advanced parsing with abstraction classes for text chunking.

**Usage example:**
```bash
# Export environment keys (comma-separated)
export GEMINI_API_KEYS="key1,key2,key3"

# Run parser for Popeliuha files
uv run python tools/document_parsers/popeliuha_pdf_parser.py
```

### 2. `web_scrapers/` (Web Page Parsing)
Scripts for extracting text articles from websites using BeautifulSoup.

- **`run_web_parsers.py`**: Main entry point. Calls submodules (`dou.py`, `qalight.py`, `gitbook.py`) to collect content and remove navigation elements.

**Usage example:**
```bash
uv run python tools/web_scrapers/run_web_parsers.py qalight
uv run python tools/web_scrapers/run_web_parsers.py dou
```

### 3. `youtube_processors/` (Audio & Subtitle Processing)
Tools for downloading YouTube content and transcribing it.

- **`fetch_popeliuha.py`**: Downloads subtitles (VTT) and audio (.m4a) from provided links.
- **`whisper_transcribe.py`**: Locally transcribes audio files to text using the OpenAI Whisper model. Used for videos without embedded subtitles.
- **`cleanup_popeliuha.py`**: Cleans VTT files from timestamps.

**Usage example:**
```bash
uv run python tools/youtube_processors/whisper_transcribe.py --input "dataset/youtube/audio/lecture.m4a"
```

### 4. `qa_and_formatters/` (Markdown Validation)
Scripts for checking generated files for syntax errors.

- **`check_broken_code.py` / `merge_code_blocks.py`**: Finds and merges broken code blocks (```) caused by chunking.
- **`check_broken_links.py`**: Validates the presence of local images referenced in text files.

**Usage example:**
```bash
uv run python tools/qa_and_formatters/check_broken_code.py --dir "dataset/articles"
```

### 5. `dataset_utils/` (Helper Tools)
Utilities for metadata and API keys.

- **`extract_popeliuha_links.py`**: Unpacks `.xlsx` files as archives, extracts Google Slides hyperlinks from `sharedStrings.xml` and `sheet1.xml.rels`, and formats direct download links.
- **`test_keys.py`**: Validates Gemini API keys and checks remaining quotas.

**Usage example:**
```bash
uv run python tools/dataset_utils/test_keys.py
```

### 6. `deprecated/` (Obsolete Tools)
Contains scripts that are non-functional or outdated in the current architecture. This includes experiments with `marker-pdf` (caused OOM and required llama.cpp), `MinerU`, `Docling`, and cloud environment setups (Colab).
