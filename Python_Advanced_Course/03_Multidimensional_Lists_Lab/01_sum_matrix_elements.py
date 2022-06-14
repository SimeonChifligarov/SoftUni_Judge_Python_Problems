rows, cols = [int(el) for el in input().split(", ")]

matrix = []

for _ in range(rows):
    row = [int(el) for el in input().split(", ")]
    matrix.append(row)

sum_of_matrix_elements = 0

for row in matrix:
    sum_of_matrix_elements += sum(row)

print(sum_of_matrix_elements)
print(matrix)
