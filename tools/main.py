import sys
import asyncio
import logging
import argparse
import os
import shutil

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

async def main():
    parser = argparse.ArgumentParser(description="Modular Parser Entry Point")
    subparsers = parser.add_subparsers(dest="resource", required=True, help="Target resource to parse")

    # QALight command
    qalight_parser = subparsers.add_parser("qalight", help="Parse qalight.ua knowledge base")
    
    # DOU command
    dou_parser = subparsers.add_parser("dou", help="Parse dou.ua QA articles")

    # PDF command
    pdf_parser = subparsers.add_parser("pdf", help="Convert local PDFs to Markdown")

    args = parser.parse_args()

    if args.resource == "qalight":
        from parsers.qalight import QalightParser
        
        # Clear the old dataset structure for idempotency
        target_dir = "dataset/qalight"
        if os.path.exists(target_dir):
            logger.info(f"Clearing old dataset directory: {target_dir}")
            shutil.rmtree(target_dir)
            
        parser_obj = QalightParser(output_dir=target_dir)
        try:
            await parser_obj.run()
        finally:
            await parser_obj.close()
            
    elif args.resource == "dou":
        from parsers.dou import DouParser
        
        target_dir = "dataset/dou/articles"
        if os.path.exists(target_dir):
            logger.info(f"Clearing old dataset directory: {target_dir}")
            shutil.rmtree(target_dir)
            
        parser_obj = DouParser(output_dir=target_dir)
        try:
            await parser_obj.run()
        finally:
            await parser_obj.close()
            
    elif args.resource == "pdf":
        from parsers.pdf import PdfParser
        parser_obj = PdfParser(input_dir="dataset/books_pdf/raw", output_dir="dataset/books_pdf")
        try:
            await parser_obj.run()
        finally:
            await parser_obj.close()
            
    else:
        logger.error(f"Unknown resource: {args.resource}")
        sys.exit(1)

if __name__ == "__main__":
    # Fix for Windows / some environments where asyncio loop throws errors on exit
    if sys.platform.startswith("win"):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
