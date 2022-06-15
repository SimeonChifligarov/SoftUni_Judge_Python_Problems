rows, cols = [int(el) for el in input().split(", ")]

matrix = []

for _ in range(rows):
    row = [int(el) for el in input().split(", ")]
    matrix.append(row)

# print(matrix)

current_position = (0, 0)

max_sum = -1_000_000  # TODO import sys.maxsize with minus
max_sum_position_top_left = None

for current_row in range(len(matrix) - 1):
    for current_col in range(len(matrix[current_row]) - 1):
        current_position = (current_row, current_col)
        current_sum = matrix[current_row][current_col] + matrix[current_row][current_col+1] + matrix[current_row+1][current_col] + matrix[current_row+1][current_col+1]
        if current_sum > max_sum:
            max_sum = current_sum
            max_sum_position_top_left = current_position

max_sum_row, max_sum_col = max_sum_position_top_left
print(matrix[max_sum_row][max_sum_col], matrix[max_sum_row][max_sum_col+1])
print(matrix[max_sum_row+1][max_sum_col], matrix[max_sum_row+1][max_sum_col+1])
print(max_sum)
