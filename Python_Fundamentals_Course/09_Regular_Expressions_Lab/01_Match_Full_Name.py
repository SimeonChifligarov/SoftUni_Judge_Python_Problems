import re

names = input()
pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"

correct_names = re.findall(pattern, names)
print(*correct_names)
