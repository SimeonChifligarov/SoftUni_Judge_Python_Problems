rows, cols = [int(el) for el in input().split()]

matrix = []

for _ in range(rows):
    row = [int(el) for el in input().split()]
    matrix.append(row)

# print(matrix)

current_position = (0, 0)

max_sum_three_by_three = -1_000_000  # TODO import sys maxsize with minus
max_sum_position = (0, 0)

for i in range(rows - 2):
    for j in range(cols - 2):
        current_position = (i, j)
        current_sum = matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2] + matrix[i + 1][j] + matrix[i + 1][j + 1] + \
                      matrix[i + 1][j + 2] + matrix[i + 2][j] + matrix[i + 2][j + 1] + matrix[i + 2][j + 2]
        if current_sum > max_sum_three_by_three:
            max_sum_three_by_three = current_sum
            max_sum_position = current_position

max_sum_row, max_sum_col = max_sum_position
print(f"Sum = {max_sum_three_by_three}")
print(matrix[max_sum_row][max_sum_col], matrix[max_sum_row][max_sum_col + 1], matrix[max_sum_row][max_sum_col + 2])
print(matrix[max_sum_row + 1][max_sum_col], matrix[max_sum_row + 1][max_sum_col + 1],
      matrix[max_sum_row + 1][max_sum_col + 2])
print(matrix[max_sum_row + 2][max_sum_col], matrix[max_sum_row + 2][max_sum_col + 1],
      matrix[max_sum_row + 2][max_sum_col + 2])
