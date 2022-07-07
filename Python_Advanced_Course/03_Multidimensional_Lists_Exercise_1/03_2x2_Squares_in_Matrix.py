rows, cols = [int(el) for el in input().split()]

matrix = []

for _ in range(rows):
    row = input().split()
    matrix.append(row)

# print(matrix)

count_of_equal_chars_two_by_two = 0

for i in range(len(matrix) - 1):
    for j in range(len(matrix[i]) - 1):
        if matrix[i][j] == matrix[i][j + 1] == matrix[i + 1][j] == matrix[i + 1][j + 1]:
            count_of_equal_chars_two_by_two += 1

print(count_of_equal_chars_two_by_two)
