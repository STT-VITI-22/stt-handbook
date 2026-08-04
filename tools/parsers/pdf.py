import os
import asyncio
import logging
from slugify import slugify

logger = logging.getLogger(__name__)

class PdfParser:
    """
    Parser for local PDF files using pymupdf4llm to convert them into Markdown.
    """
    def __init__(self, input_dir: str = "dataset/books_pdf/raw", output_dir: str = "dataset/books_pdf"):
        self.input_dir = input_dir
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        
    def _clean_slug(self, filename: str) -> str:
        name_without_ext = os.path.splitext(filename)[0]
        safe = slugify(name_without_ext)
        return safe or f"pdf-{hash(filename) % 10000}"

    async def _process_pdf(self, filename: str):
        import pymupdf4llm
        
        filepath = os.path.join(self.input_dir, filename)
        logger.info(f"Processing PDF: {filename}...")
        
        try:
            # pymupdf4llm performs layout analysis and extracts tables, text, headers robustly.
            # Running in executor since to_markdown is synchronous and CPU bound.
            loop = asyncio.get_event_loop()
            md_text = await loop.run_in_executor(None, pymupdf4llm.to_markdown, filepath)
            
            safe_filename = self._clean_slug(filename)
            out_filepath = os.path.join(self.output_dir, f"{safe_filename}.md")
            
            with open(out_filepath, 'w', encoding='utf-8') as f:
                f.write(f"# {filename}\n\n**Source PDF:** {filename}\n\n---\n\n{md_text}")
                
            logger.info(f"Saved Markdown: {out_filepath}")
        except Exception as e:
            logger.error(f"Failed to process {filename}: {e}")

    async def run(self):
        if not os.path.exists(self.input_dir):
            logger.error(f"Input directory does not exist: {self.input_dir}")
            return
            
        pdf_files = [f for f in os.listdir(self.input_dir) if f.lower().endswith('.pdf')]
        if not pdf_files:
            logger.warning(f"No PDF files found in {self.input_dir}")
            return
            
        logger.info(f"Found {len(pdf_files)} PDF files in {self.input_dir}")
        
        tasks = []
        for pdf_file in pdf_files:
            tasks.append(self._process_pdf(pdf_file))
            
        # Process them concurrently
        await asyncio.gather(*tasks)
        logger.info("PDF conversion complete.")

    async def close(self):
        # Interface compliance
        pass
