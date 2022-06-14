# Use nested comprehension for that problem (from requirements)

rows = int(input())
matrix = []

for i in range(rows):
    row = [int(num) for num in input().split(", ")]
    matrix.append(row)

evens = [[x for x in row if x % 2 == 0] for row in matrix]

print(evens)
