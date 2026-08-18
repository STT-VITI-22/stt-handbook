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

    # GitBook command
    gitbook_parser = subparsers.add_parser("gitbook", help="Parse QA Bible GitBook")

    args = parser.parse_args()

    if args.resource == "qalight":
        from web_scrapers.qalight import QalightParser
        
        target_dir = "dataset/articles/qalight"
        if os.path.exists(target_dir):
            logger.info(f"Clearing old dataset directory: {target_dir}")
            shutil.rmtree(target_dir)
            
        parser_obj = QalightParser(output_dir=target_dir)
        try:
            await parser_obj.run()
        finally:
            await parser_obj.close()
            
    elif args.resource == "dou":
        from web_scrapers.dou import DouParser
        
        target_dir = "dataset/articles/dou/articles"
        if os.path.exists(target_dir):
            logger.info(f"Clearing old dataset directory: {target_dir}")
            shutil.rmtree(target_dir)
            
        parser_obj = DouParser(output_dir=target_dir)
        try:
            await parser_obj.run()
        finally:
            await parser_obj.close()
            
    elif args.resource == "gitbook":
        from web_scrapers.gitbook import GitBookParser
        
        target_dir = "dataset/articles/QA_Bible"
        # We do not rmtree this directory because it contains user files like README.md
            
        parser_obj = GitBookParser(base_url="https://vladislaveremeev.gitbook.io/qa_bible", output_dir=target_dir)
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
