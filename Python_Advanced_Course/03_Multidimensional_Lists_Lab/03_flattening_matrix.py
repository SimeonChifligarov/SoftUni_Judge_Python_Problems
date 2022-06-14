rows = int(input())
matrix = []

for i in range(rows):
    row = [int(num) for num in input().split(", ")]
    matrix.append(row)

flattened_matrix = [num for sublist in matrix for num in sublist]

print(flattened_matrix)
