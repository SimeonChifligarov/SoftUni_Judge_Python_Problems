size_of_square_matrix = int(input())

matrix = []

for _ in range(size_of_square_matrix):
    row = [int(el) for el in input().split()]
    matrix.append(row)

primary_diagonal = []
secondary_diagonal = []

for i in range(size_of_square_matrix):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][size_of_square_matrix - 1 - i])

sum_of_primary_diagonal = sum(primary_diagonal)
sum_of_secondary_diagonal = sum(secondary_diagonal)

abs_difference_of_diagonals = abs(sum_of_primary_diagonal - sum_of_secondary_diagonal)
print(abs_difference_of_diagonals)
