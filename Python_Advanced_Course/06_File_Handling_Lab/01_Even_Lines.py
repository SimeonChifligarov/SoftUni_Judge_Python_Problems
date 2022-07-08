import re

with open('text') as file:
    lines = file.readlines()

for index, line in enumerate (lines):
    if index % 2 != 0:
        continue

    line = re.sub(r"[\?,\!\.-]", '@', line)
    line = ' '.join(reversed(line.split()))

    print(line.strip())