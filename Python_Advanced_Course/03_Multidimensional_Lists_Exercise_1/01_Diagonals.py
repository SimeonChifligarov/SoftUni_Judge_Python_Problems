matrix_size = int(input())
matrix = []
primary_diagonal = []
secondary_diagonal = []

for i in range(matrix_size):
    matrix.append([int(el) for el in input().split(', ')])
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][matrix_size - i - 1])

# print(matrix)
# print(primary_diagonal)
# print(secondary_diagonal)

print(f'Primary diagonal: {", ".join([str(el) for el in primary_diagonal])}. Sum: {sum(primary_diagonal)}')
print(f'Secondary diagonal: {", ".join([str(el) for el in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}')
