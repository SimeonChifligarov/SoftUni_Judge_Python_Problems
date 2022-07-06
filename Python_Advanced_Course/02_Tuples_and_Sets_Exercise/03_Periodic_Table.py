number_of_lines = int(input())

unique_chemical_elements = set()

for _ in range(number_of_lines):
    line = input().split()
    for el in line:
        unique_chemical_elements.add(el)

print(*unique_chemical_elements, sep='\n')
