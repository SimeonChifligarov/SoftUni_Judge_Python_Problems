names_count = int(input())

unique_names = set()

for _ in range(names_count):
    name = input()
    unique_names.add(name)

print(*unique_names, sep="\n")
