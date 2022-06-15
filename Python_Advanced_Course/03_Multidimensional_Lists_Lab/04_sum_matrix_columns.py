rows, cols = [int(el) for el in input().split(", ")]

matrix = []

for _ in range(rows):
    row = [int(el) for el in input().split()]
    matrix.append(row)

all_columns_sums = []

for j in range(cols):
    current_column_sum = 0
    for i in range(rows):
        current_column_sum += matrix[i][j]
    all_columns_sums.append(current_column_sum)

print(*all_columns_sums, sep="\n")
