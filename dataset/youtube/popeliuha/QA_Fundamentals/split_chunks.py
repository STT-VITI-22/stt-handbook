import re
import os

with open('/home/liulmiti/workspace/22_dep/stt/dataset/dataset/youtube/popeliuha/QA_Fundamentals/8-_Створення_Чек-ліста_на_практиці.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Separate the header part
lines = text.split('\n')
header = lines[:4]
content = '\n'.join(lines[4:])

words = content.split()
chunk_size = 1200
chunks = []

for i in range(0, len(words), chunk_size):
    chunk = ' '.join(words[i:i+chunk_size])
    chunks.append(chunk)

with open('header.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(header) + '\n')

for idx, chunk in enumerate(chunks, 1):
    with open(f'chunk_{idx:02d}.txt', 'w', encoding='utf-8') as f:
        f.write(chunk)
print(f"Created {len(chunks)} chunks.")
