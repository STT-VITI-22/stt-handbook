import sys
content = sys.stdin.read()
with open('formatted.md', 'a', encoding='utf-8') as f:
    f.write(content + '\n')
