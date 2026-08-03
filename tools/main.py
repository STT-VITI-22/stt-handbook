#!/usr/bin/env python3
"""
Main Entry Point: Universal AI-Driven ETL Pipeline
Supports modular execution phases (discover -> classify -> download) 
and dynamic dataset structuring strategies (source vs topic).
"""
import argparse
import asyncio
import yaml
import json
import logging
import os
import sys

# Import custom ETL modules
from etl.discovery import discover_links
from etl.ai import classify_articles
from etl.downloader import download_all

# Configure standard logging to replace raw print statements
logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
logger = logging.getLogger("ETL_Main")

def load_config(config_path: str) -> dict:
    """Loads the YAML configuration file containing target sources."""
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except Exception as e:
        logger.error(f"Failed to load config {config_path}: {e}")
        sys.exit(1)

async def main():
    parser = argparse.ArgumentParser(description="Universal AI-Driven ETL Pipeline")
    parser.add_argument('action', choices=['discover', 'classify', 'download', 'run_all'], 
                        help="The pipeline phase to execute.")
    parser.add_argument('--config', default="tools/sources.yaml", help="Path to sources configuration.")
    parser.add_argument('--input', default="raw_discovery.jsonl", help="Input file for phases.")
    parser.add_argument('--output', default="manifest.jsonl", help="Output file for phases.")
    parser.add_argument('--outdir', default="data", help="Target directory for downloaded markdown files.")
    parser.add_argument('--strategy', choices=['source', 'topic'], default='topic', 
                        help="Structuring strategy: 'source' preserves the original website menu paths, 'topic' uses strict AI categorization (e.g. ISTQB domains).")
    
    args = parser.parse_args()
    config = load_config(args.config)
    
    # ---------------------------------------------------------
    # PHASE 1: DISCOVER
    # ---------------------------------------------------------
    if args.action in ['discover', 'run_all']:
        logger.info("=== PHASE: DISCOVERY ===")
        discovered = await discover_links(config.get('sources', []))
        
        with open(args.input, 'w', encoding='utf-8') as f:
            for item in discovered:
                f.write(json.dumps(item, ensure_ascii=False) + '\n')
        logger.info(f"Discovery complete. Found {len(discovered)} raw links. Saved to {args.input}")

    # ---------------------------------------------------------
    # PHASE 2: CLASSIFY
    # ---------------------------------------------------------
    if args.action in ['classify', 'run_all']:
        logger.info("=== PHASE: AI CLASSIFICATION ===")
        if not os.path.exists(args.input):
            logger.error(f"Input file {args.input} not found. Did you run 'discover' phase?")
            sys.exit(1)
            
        with open(args.input, 'r', encoding='utf-8') as f:
            articles = [json.loads(line) for line in f]
            
        classified = await classify_articles(articles)
        
        with open(args.output, 'w', encoding='utf-8') as f:
            for item in classified:
                item.pop('id', None) # Clean up temporary batch IDs
                f.write(json.dumps(item, ensure_ascii=False) + '\n')
        logger.info("Classification complete.")

    # ---------------------------------------------------------
    # PHASE 3: DOWNLOAD & EXTRACTION
    # ---------------------------------------------------------
    if args.action in ['download', 'run_all']:
        logger.info("=== PHASE: DOWNLOAD & EXTRACTION ===")
        if not os.path.exists(args.output):
            logger.error(f"Manifest file {args.output} not found. Did you run 'classify' phase?")
            sys.exit(1)
            
        # ---------------------------------------------------------
        # IDEMPOTENCY ENFORCEMENT:
        # Before downloading new files, we must completely wipe the target output directory.
        # This prevents "ghost" files from previous pipeline runs (where an article might have 
        # been classified into a different folder) from persisting in the final dataset.
        # ---------------------------------------------------------
        if os.path.exists(args.outdir):
            import shutil
            logger.info(f"Clearing output directory: {args.outdir}")
            shutil.rmtree(args.outdir)
        os.makedirs(args.outdir, exist_ok=True)
            
        with open(args.output, 'r', encoding='utf-8') as f:
            # Load only the articles that were approved by the AI
            articles = [json.loads(line) for line in f if json.loads(line).get('keep')]
            
        await download_all(articles, args.outdir, args.strategy, config.get('sources', []))
        logger.info("Download complete.")

if __name__ == "__main__":
    asyncio.run(main())
