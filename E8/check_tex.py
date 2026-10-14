import re

with open('main.tex') as f:
    text = f.read()

# Replace unescaped % that looks like a percentage number e.g. 88%
pattern = r'(?<!\\)%'
matches = list(re.finditer(pattern, text))
print(f'Total unescaped %: {len(matches)}')
for m in matches:
    start = max(0, m.start() - 30)
    end = min(len(text), m.end() + 30)
    print(repr(text[start:end]))
