import re
import sys
import webvtt

def vtt_to_text(vtt_file):
    try:
        vtt = webvtt.read(vtt_file)
    except Exception as e:
        print(f"Error reading {vtt_file}: {e}")
        return
    
    text_lines = []
    last_line = ""
    for caption in vtt:
        # Auto-generated YouTube subs often have <c> tags and duplicates
        clean_text = re.sub(r'<[^>]+>', '', caption.text)
        # Split by newlines in case it's multiline
        lines = [line.strip() for line in clean_text.split('\n') if line.strip()]
        
        for line in lines:
            # Avoid repeating the exact same line sequentially (common in rolling auto-subs)
            if line and line != last_line:
                text_lines.append(line)
                last_line = line

    return " ".join(text_lines)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python vtt_to_text.py <file.vtt>")
        sys.exit(1)
    
    print(vtt_to_text(sys.argv[1]))
