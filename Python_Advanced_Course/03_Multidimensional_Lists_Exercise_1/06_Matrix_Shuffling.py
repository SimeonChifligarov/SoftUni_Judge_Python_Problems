END_COMMAND = "END"
SWAP_COMMAND = "swap"
INVALID_COMMAND_MESSAGE = "Invalid input!"

rows, cols = [int(el) for el in input().split()]

matrix = []

for _ in range(rows):
    row = input().split()
    matrix.append(row)

# print(matrix)

while True:
    command_data = input()
    if command_data == END_COMMAND:
        break

    if not command_data.startswith(SWAP_COMMAND):
        print(INVALID_COMMAND_MESSAGE)
        continue

    try:
        row_1, col_1, row_2, col_2 = [int(el) for el in command_data.split()[1:]]
        if 0 <= row_1 < rows and 0 <= row_2 < rows and 0 <= col_1 < cols and 0 <= col_2 < cols:
            matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]
            for r in matrix:
                print(*r)
        else:
            print(INVALID_COMMAND_MESSAGE)
    except:
        print(INVALID_COMMAND_MESSAGE)
        continue
