size_of_square_matrix = int(input())

matrix = []

for _ in range(size_of_square_matrix):
    row = [int(el) for el in input().split()]
    matrix.append(row)

primary_diagonal = []

for i in range(len(matrix)):
    primary_diagonal.append(matrix[i][i])

sum_of_primary_diagonal = sum(primary_diagonal)
print(sum_of_primary_diagonal)
