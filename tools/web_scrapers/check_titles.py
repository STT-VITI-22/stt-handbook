import os
import glob
import re

dir_path = 'dataset/youtube/popeliuha'
files = glob.glob(os.path.join(dir_path, '*.md'))

special_chars = set()
titles_with_symbols = []

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        first_line = f.readline().strip()
        if first_line.startswith('# '):
            original_title = first_line[2:] # remove '# '
            
            # Find all characters that are NOT alphanumeric, space, or standard dash
            # Also exclude standard Ukrainian/English letters
            # Let's just find anything outside \w, \s, -
            # Actually, standard regex \w includes underscores and digits.
            chars = re.findall(r'[^a-zA-Z0-9\u0400-\u04FF\s\-]', original_title)
            
            if chars:
                special_chars.update(chars)
                titles_with_symbols.append(original_title)

print("Знайдені спеціальні символи в оригінальних заголовках:")
print(" ".join(sorted(list(special_chars))))
print("\nПриклади заголовків із цими символами:")
for t in titles_with_symbols[:20]: # show first 20 for context
    print(f" - {t}")
print(f"...(загалом {len(titles_with_symbols)} заголовків із спецсимволами)")
