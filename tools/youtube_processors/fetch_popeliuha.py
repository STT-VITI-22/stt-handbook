import json
import re
import sys
import time
import os
import subprocess
import webvtt

# Obvious non-educational/vlog content
EXCLUDE_KEYWORDS = [
    'як вижити на іт-конференції',
    'a day at it events',
    'порад як зробити',
    'розіграш',
    'giveaway'
]

def is_qa_related(title):
    title_lower = title.lower()
    for kw in EXCLUDE_KEYWORDS:
        if kw in title_lower:
            return False
    return True

def clean_filename(title):
    # Keep only alphanumeric and spaces/dashes
    clean = re.sub(r'[^a-zA-Z0-9\u0400-\u04FF\s\-]', '', title)
    return clean.strip()[:100]

def parse_vtt(vtt_file):
    try:
        vtt = webvtt.read(vtt_file)
        text_lines = []
        last_line = ""
        for caption in vtt:
            clean_text = re.sub(r'<[^>]+>', '', caption.text)
            lines = [line.strip() for line in clean_text.split('\n') if line.strip()]
            for line in lines:
                if line and line != last_line:
                    text_lines.append(line)
                    last_line = line
        return " ".join(text_lines)
    except Exception as e:
        return None

def main():
    with open('local-dev/popeliuha_videos.json', 'r', encoding='utf-8') as f:
        videos = [json.loads(line) for line in f if line.strip()]

    target_dir = 'dataset/articles/youtube_popeliuha'
    os.makedirs(target_dir, exist_ok=True)
    
    missing_subs = []
    
    # Filter videos
    qa_videos = [v for v in videos if is_qa_related(v.get('title', ''))]
    print(f"Total QA related videos to fetch: {len(qa_videos)} out of {len(videos)}")
    
    for i, v in enumerate(qa_videos, 1):
        title = v.get('title', 'Unknown')
        url = v.get('url')
        print(f"[{i}/{len(qa_videos)}] Processing: {title}")
        
        safe_title = clean_filename(title)
        md_file = os.path.join(target_dir, f"{safe_title}.md")
        if os.path.exists(md_file):
            print("  -> Already exists, skipping.")
            continue
            
        # Download VTT using yt-dlp (uk, ru, en)
        vtt_base = os.path.join(target_dir, safe_title)
        cmd = [
            'python3', '-m', 'yt_dlp',
            '--write-auto-subs', '--write-subs', '--skip-download',
            '--sub-format', 'vtt', '--sub-langs', 'uk,ru,en',
            '-o', f'{vtt_base}.%(ext)s', url
        ]
        
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        # Check which language was downloaded
        vtt_file = None
        for lang in ['uk', 'ru', 'en']:
            candidate = f"{vtt_base}.{lang}.vtt"
            if os.path.exists(candidate):
                vtt_file = candidate
                break
                
        if vtt_file:
            text = parse_vtt(vtt_file)
            if text:
                with open(md_file, 'w', encoding='utf-8') as mf:
                    mf.write(f"# {title}\n\n")
                    mf.write(f"Source: {url}\n\n")
                    mf.write(text + "\n")
                print("  -> Success")
            else:
                print("  -> Failed to parse VTT")
                missing_subs.append(title)
                
            # Cleanup all VTT files for this video
            for lang in ['uk', 'ru', 'en']:
                candidate = f"{vtt_base}.{lang}.vtt"
                if os.path.exists(candidate):
                    os.remove(candidate)
        else:
            print("  -> No subtitles found")
            missing_subs.append(title)
            
        time.sleep(2) # Prevent rate limits
        
    if missing_subs:
        with open('local-dev/missing_subtitles.log', 'w', encoding='utf-8') as f:
            f.write("\n".join(missing_subs))
        print(f"Logged {len(missing_subs)} videos with missing subtitles.")

if __name__ == "__main__":
    main()
