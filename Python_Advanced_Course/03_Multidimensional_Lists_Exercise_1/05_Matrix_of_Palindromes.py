rows, cols = [int(el) for el in input().split()]

# print(rows, cols)

matrix = []

for i in range(rows):
    current_row = []

    for j in range(cols):
        current_row.append(f'{chr(97 + i)}{chr(97 + i + j)}{chr(97 + i)}')

    matrix.append(current_row)

# print(matrix)

[print(*row) for row in matrix]
