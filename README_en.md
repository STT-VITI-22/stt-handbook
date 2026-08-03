# QA Knowledge Base Dataset & AI Pipeline

This repository contains a curated dataset of materials for QA engineers and a universal AI-Driven ETL pipeline for autonomous data collection.

## Dataset Structure (Single Branch)

We have abandoned the use of different Git branches for different data sorting methods. The dataset structure is now generated dynamically during the pipeline execution. All data is stored in the `data/` directory, and its architecture depends on your chosen strategy:

1. **`source` Strategy (By Source):**
   Materials are stored in folders corresponding to their original sources and website categories (e.g., `data/qalight_baza/automation/`). This preserves the authors' original intent and site hierarchy.
2. **`topic` Strategy (By ISTQB Topics):**
   Artificial Intelligence analyzes the content of each article and automatically categorizes them into 13 strictly defined domains (e.g., `data/test_levels/`, `data/api_testing/`).

## Universal Collection Tool (`tools/main.py`)

The pipeline is fully modular and controlled by an external config `tools/sources.yaml`. In the config, you specify the URL and CSS selectors for finding articles and mapping category hierarchies, making the script compatible with any blog or knowledge base.

The pipeline operates in three stages:
1. **Discover:** Asynchronous link collection (`httpx` + `BeautifulSoup4`) based on selectors from `sources.yaml`. It also intelligently extracts parent category names to recreate the original menu hierarchy.
2. **AI Classify:** Analysis via Gemini API (google-genai). Thanks to Structured Outputs (Pydantic), the model strictly adheres to the ISTQB syllabus defined in its prompt. It discards junk (marketing, pure software engineering) and assigns relevant articles to the correct category. A sliding window algorithm protects against API rate limits (5 requests per minute).
3. **Download & Extract:** Hybrid text extraction. First, it attempts an exact CSS selector extraction from the config (cleaned via `markdownify`), guaranteeing the preservation of lists and code examples. If missing, it falls back to the universal `trafilatura` algorithm.

## Dependencies and Usage

Install dependencies in a virtual environment:
```bash
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

The AI classification stage requires an API key:
```bash
export GEMINI_API_KEY="your_key"
```

Run the pipeline (all stages at once, grouped by source hierarchy):
```bash
python tools/main.py run_all --strategy source
```
*(For all available options, use `python tools/main.py -h`)*
