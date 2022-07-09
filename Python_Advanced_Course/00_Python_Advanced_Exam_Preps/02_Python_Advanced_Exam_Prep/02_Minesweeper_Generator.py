def is_index_in_range(index, square_matrix):
    return 0 <= index < len(square_matrix)


mapper = {
    "up": (1, 0),
    "down": (-1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "ur": (1, 1),
    "ul": (1, -1),
    "dr": (-1, 1),
    "dl": (-1, -1),
}

size_of_square_matrix = int(input())
number_of_bombs = int(input())

bomb_positions = []

for _ in range(number_of_bombs):
    bomb_row, bomb_col = [int(el) for el in input()[1:-1].split(", ")]
    bomb_position = (bomb_row, bomb_col)
    bomb_positions.append(bomb_position)

matrix = []

for _ in range(size_of_square_matrix):
    row = [0] * size_of_square_matrix
    matrix.append(row)

for bomb in bomb_positions:
    bomb_row, bomb_col = bomb
    matrix[bomb_row][bomb_col] = "*"

# print(matrix)

for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        if matrix[r][c] == "*":
            continue

        for pos in mapper.values():
            current_row = r
            current_col = c
            current_row += pos[0]
            current_col += pos[1]
            if is_index_in_range(current_row, matrix) and is_index_in_range(current_col, matrix):
                if matrix[current_row][current_col] == "*":
                    matrix[r][c] += 1

for row in matrix:
    print(*row)
