import os

_, _, files = next(os.walk(input()))

by_extension = {}
for file in files:
    ext = file.split('.')[-1]

    if ext not in by_extension:
        by_extension[ext] = []

    by_extension[ext].append(file)

with open(os.path.expanduser('report.txt'), 'w') as out_file:
    for ext in sorted(by_extension.keys()):
        files = sorted(by_extension[ext])
        out_file.write(f'.{ext}\n')

        for file in files:
            out_file.write(f'- - -{file}\n')
