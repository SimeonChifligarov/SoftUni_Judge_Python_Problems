def is_coordinate_valid(x, y, mtrx):
    return 0 <= x < len(mtrx) and 0 <= y < len(mtrx[x])


END_COMMAND = 'END'
ADD_COMMAND = 'Add'
SUBTRACT_COMMAND = 'Subtract'
INVALID_COORDS_MESSAGE = 'Invalid coordinates'

matrix_row = int(input())

matrix = []

for _ in range(matrix_row):
    row = [int(el) for el in input().split()]
    matrix.append(row)

# print(matrix)

while True:
    command = input()

    if command == END_COMMAND:
        break

    command_tokens = command.split()
    real_command = command_tokens[0]
    coord_x = int(command_tokens[1])
    coord_y = int(command_tokens[2])
    value = int(command_tokens[3])

    if not is_coordinate_valid(coord_x, coord_y, matrix):
        print(INVALID_COORDS_MESSAGE)
        continue

    if real_command == ADD_COMMAND:
        matrix[coord_x][coord_y] += value
    elif real_command == SUBTRACT_COMMAND:
        matrix[coord_x][coord_y] -= value

[print(*row) for row in matrix]
