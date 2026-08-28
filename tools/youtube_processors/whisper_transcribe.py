import json
import os
import subprocess
import re
import whisper

def get_clean_name(title):
    t = title.replace('#', 'Sharp')
    t = t.replace('+', 'Plus')
    t = t.replace('&', 'and')
    t = re.sub(r'[\.\,\:\|/\\]', '-', t)
    t = re.sub(r"[\(\)\'\?\😱\u200b]", "", t)
    t = re.sub(r'\s+', '_', t.strip())
    t = re.sub(r'-+', '-', t)
    t = re.sub(r'_+', '_', t)
    return t.strip('-_')

def get_category(title):
    t_lower = title.lower()
    if any(kw in t_lower for kw in ['тест дизайн', 'equivalence', 'еквівалентн']): return 'Test_Design_Techniques'
    if any(kw in t_lower for kw in ['scrum', 'agile', 'development methodologies', 'цикл життя']): return 'Agile_and_Management'
    return 'QA_Fundamentals'

# List of purely theoretical missing videos we actually want
TARGET_TITLES = [
    "31. Equivalence Partitioning. Еквівалентне розділення",
    "30. Вступ в техніки тест дизайну - 3 категорії",
    "28. Статичні типи тестування. Рецензування",
    "26. Типи тестування, пов'язані зі змінами. Регресія. Impact Analysis",
    "25. Нефункціональні типи тестування",
    "24. Рівні тестування. Функціональні типи",
    "23. Загально про Типи тестування",
    "22. Підходи тестування",
    "21. Принципи Тестування",
    "17. Вся теорія про Дефекти / Баги",
    "15. Requirements. User Stories. Acceptance Criteria",
    "14. Тест план, Тест стратегія, Test Policy. З прикладами",
    "7. Тестова документація. Test case. Test suite. Check-list",
    "5. Scrum, Всі мітинги Скраму. Velocity, Capacity. Kanban",
    "4. Development methodologies. Sequential, iterative. Agile. V-model",
    "3. Цикл життя ПЗ і Цикл тестування"
]

def main():
    print("Loading Whisper model (small)...")
    model = whisper.load_model("small")
    
    with open('local-dev/popeliuha_videos.json', 'r', encoding='utf-8') as f:
        videos = [json.loads(line) for line in f if line.strip()]
    
    url_map = {v['title']: v['url'] for v in videos if 'title' in v}
    
    for title in TARGET_TITLES:
        url = url_map.get(title)
        if not url:
            print(f"URL not found for: {title}")
            continue
            
        cat = get_category(title)
        clean = get_clean_name(title)
        md_path = f"dataset/youtube/popeliuha/{cat}/{clean}.md"
        
        if os.path.exists(md_path):
            print(f"Already exists: {md_path}")
            continue
            
        print(f"\nProcessing: {title}")
        mp3_file = f"local-dev/{clean}.mp3"
        
        # Download audio
        cmd = [
            'python3', '-m', 'yt_dlp',
            '-x', '--audio-format', 'mp3',
            '-o', mp3_file, url
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        if os.path.exists(mp3_file):
            print("Audio downloaded. Transcribing...")
            try:
                result = model.transcribe(mp3_file, language="uk")
                text = result["text"].strip()
                
                # Write to MD
                with open(md_path, 'w', encoding='utf-8') as f:
                    f.write(f"# {title}\n\nSource: {url}\n\n{text}\n")
                print(f"Saved: {md_path}")
            except Exception as e:
                print(f"Transcription failed: {e}")
            finally:
                os.remove(mp3_file)
        else:
            print("Failed to download audio.")

if __name__ == "__main__":
    main()
