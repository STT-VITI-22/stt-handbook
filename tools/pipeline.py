import os
import json
import asyncio
import httpx
from bs4 import BeautifulSoup
import yaml
from pydantic import BaseModel, Field
import argparse
from slugify import slugify
import time
from urllib.parse import urlparse, urljoin
import trafilatura

class ArticleDecision(BaseModel):
    id: int
    keep: bool = Field(
        description="True for QA-related topics (including network/web fundamentals). False ONLY for pure development (RxJava, Android Studio, OOP paradigms) or unrelated hardware/OS topics."
    )

class BatchDecision(BaseModel):
    decisions: list[ArticleDecision]

def get_safe_filename(title: str, url: str) -> str:
    safe = slugify(title)
    if not safe and url:
        safe = slugify(url.split('/')[-2]) if url.endswith('/') else slugify(url.split('/')[-1])
    return safe or f"article-{hash(url) % 10000}"

async def discover(config_file: str, output_file: str):
    print(f"[*] Етап розвідки (Universal): Читаємо конфіг {config_file}")
    
    with open(config_file, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
        
    discovered = []
    seen_urls = set()
    
    async with httpx.AsyncClient(timeout=15.0) as client:
        for source in config.get('sources', []):
            url = source['url']
            selector = source['link_selector']
            source_name = source['name']
            
            print(f"  -> Обробка джерела: {source_name}")
            try:
                resp = await client.get(url, follow_redirects=True)
                soup = BeautifulSoup(resp.text, 'lxml')
                
                links = soup.select(selector)
                for link in links:
                    href = link.get('href')
                    if not href or href == '#': continue
                    
                    full_url = urljoin(url, href)
                    if full_url in seen_urls: continue
                    seen_urls.add(full_url)
                    
                    title = link.get_text(strip=True)
                    discovered.append({
                        "url": full_url,
                        "title": title,
                        "source_name": source_name
                    })
            except Exception as e:
                print(f"[!] Помилка розвідки {url}: {e}")

    with open(output_file, 'w', encoding='utf-8') as f:
        for item in discovered:
            f.write(json.dumps(item, ensure_ascii=False) + '\n')
    print(f"[+] Знайдено унікальних статей: {len(discovered)}. Збережено у {output_file}")

def classify(input_file: str, output_file: str):
    print(f"[*] Етап класифікації (AI Filter): Читаємо {input_file}")
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("[!] GEMINI_API_KEY відсутній. Перервано.")
        return
        
    with open(input_file, 'r', encoding='utf-8') as f:
        articles = [json.loads(line) for line in f]
        
    classified = []
    from google import genai
    from google.genai import types
    client = genai.Client()
    
    for i, a in enumerate(articles):
        a['id'] = i
        
    chunk_size = 30
    request_times = []
    
    for i in range(0, len(articles), chunk_size):
        current_time = time.time()
        request_times = [t for t in request_times if current_time - t < 60]
        
        if len(request_times) >= 4:
            sleep_time = 60 - (current_time - request_times[0])
            if sleep_time > 0:
                print(f"[*] Обмеження API (5 RPM): очікування {sleep_time:.1f} сек...")
                time.sleep(sleep_time)
        
        request_times.append(time.time())
        chunk = articles[i:i+chunk_size]
        prompt_data = [{"id": a['id'], "title": a['title'], "url": a['url']} for a in chunk]
        
        prompt = f"Filter these articles for a QA Engineer Knowledge Base. Keep QA/testing topics and network fundamentals. Discard pure software engineering or unrelated topics.\n\n{json.dumps(prompt_data, ensure_ascii=False)}"
        
        print(f"[*] Відправляємо пакет {i//chunk_size + 1} ({len(chunk)} статей)...")
        try:
            response = client.models.generate_content(
                model='gemini-3.6-flash',
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=BatchDecision,
                    temperature=0.1
                ),
            )
            res_dict = json.loads(response.text)
            decision_map = {d['id']: d for d in res_dict['decisions']}
            
            for a in chunk:
                d = decision_map.get(a['id'])
                a['keep'] = d['keep'] if d else False
                classified.append(a)
                print(f"  {'v' if a['keep'] else 'x'} {a['title'][:45]}...")
                
        except Exception as e:
            print(f"[!] Помилка пакета: {e}")
            for a in chunk:
                a['keep'] = False
                classified.append(a)
            
    with open(output_file, 'w', encoding='utf-8') as f:
        for item in classified:
            item.pop('id', None)
            f.write(json.dumps(item, ensure_ascii=False) + '\n')
    print(f"[+] Фільтрацію завершено. Збережено: {output_file}")

async def download_article(client, item, base_dir):
    if not item.get("keep"):
        return
        
    url = item['url']
    source_name = item['source_name']
    target_dir = os.path.join(base_dir, source_name)
    os.makedirs(target_dir, exist_ok=True)
    
    try:
        resp = await client.get(url, follow_redirects=True)
        # Використовуємо trafilatura для універсальної екстракції головного тексту з будь-якого сайту
        markdown_text = trafilatura.extract(resp.text, output_format="markdown", include_links=True)
        
        if not markdown_text:
            print(f"[!] Trafilatura не знайшла текст на {url}")
            return
            
        safe_filename = get_safe_filename(item['title'], url)
        filepath = os.path.join(target_dir, f"{safe_filename}.md")
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# {item['title']}\n\n**Source:** {url}\n\n---\n\n{markdown_text}")
        print(f"[+] Збережено: {safe_filename}.md -> {target_dir}")
    except Exception as e:
        print(f"[!] Помилка завантаження {url}: {e}")

async def download(input_file: str, base_dir: str):
    print(f"[*] Етап завантаження: Читаємо маніфест {input_file}")
    with open(input_file, 'r', encoding='utf-8') as f:
        articles = [json.loads(line) for line in f if json.loads(line).get("keep")]
        
    print(f"[*] Схвалено статей: {len(articles)}. Починаємо паралельне завантаження...")
    async with httpx.AsyncClient(timeout=20.0, limits=httpx.Limits(max_connections=5)) as client:
        tasks = [download_article(client, a, base_dir) for a in articles]
        await asyncio.gather(*tasks)
    print(f"[+] Усі файли успішно завантажені!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Universal AI-Driven ETL Pipeline")
    parser.add_argument('action', choices=['discover', 'classify', 'download'])
    parser.add_argument('--config', default="tools/sources.yaml")
    parser.add_argument('--input', default="raw_discovery.jsonl")
    parser.add_argument('--output', default="manifest.jsonl")
    parser.add_argument('--outdir', default="../data")
    
    args = parser.parse_args()
    
    if args.action == 'discover':
        asyncio.run(discover(args.config, args.output))
    elif args.action == 'classify':
        classify(args.input, args.output)
    elif args.action == 'download':
        asyncio.run(download(args.input, args.outdir))
