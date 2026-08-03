# QA Dataset ETL Pipeline

A pipeline for collecting, classifying, and formatting QA articles into a structured dataset.

## Pipeline Structure

The process is orchestrated by `tools/main.py` and consists of three stages:

### 1. Discovery (`etl/discovery.py`)
Collects article URLs based on configurations in `tools/sources.yaml`. It uses asynchronous requests (`httpx`) and DOM parsing (`BeautifulSoup`) to extract links and the original site menu structure.

### 2. Classification (`etl/ai.py`)
Classifies the collected articles into ISTQB Foundation Level categories using the Gemini API.
- **Content Fetching:** Downloads the first 500 characters of each article to provide context to the LLM. This helps the model determine the topic more accurately than using titles alone.
- **Categorization:** Uses Structured Outputs (Pydantic) to validate the selected category against a list of ISTQB domains. Articles marked as irrelevant by the model are discarded (`keep: False`).
- **Course Routing:** If a URL contains `/kursy/`, the article automatically receives the `courses` category, overriding the LLM's decision.
- **Rate Limiting:** A built-in algorithm throttles API requests to prevent 429 (Too Many Requests) errors.

### 3. Extraction & Formatting (`etl/downloader.py`)
Downloads the HTML content of the articles and converts it to Markdown.
- **Cleanup:** The target directory is completely deleted and recreated before downloading begins.
- **Markdown Conversion:** Uses the `markdownify` library. The `keep_inline_images_in` parameter is applied to preserve `<img>` tags located inside headers or paragraphs. Literal HTML tags in the text (e.g., `<head>`) are escaped with backticks.

## Usage

Set the environment variable with your API key:
```bash
export GEMINI_API_KEY="your_api_key_here"
```

Run the pipeline:
```bash
uv run python tools/main.py run_all --strategy topic
```

### Save Strategies (`--strategy`)
- `topic` (default): Distributes files into directories based on the ISTQB categories determined during classification.
- `source`: Saves files in directories that mirror the original website's structure.
All materials categorized as `courses` are saved in a separate dedicated folder regardless of the chosen strategy.
