def is_index_in_range(index, square_matrix):
    return 0 <= index < len(square_matrix)


mapper_position = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "ul": (-1, -1),
    "ur": (-1, 1),
    "dl": (1, -1),
    "dr": (1, 1),
}

square_matrix_size = int(input())

matrix = []

for _ in range(square_matrix_size):
    row = [int(el) for el in input().split()]
    matrix.append(row)

# print(matrix)

indexes_coordinates = input().split()
bombs_coordinates = []
for coord in indexes_coordinates:
    current_row, current_col = [int(el) for el in coord.split(",")]
    bombs_coordinates.append((current_row, current_col))

for bomb in bombs_coordinates:
    bomb_row, bomb_col = bomb
    if is_index_in_range(bomb_row, matrix) and is_index_in_range(bomb_col, matrix):
        bomb_value = matrix[bomb_row][bomb_col]
        if bomb_value > 0:
            for direction in mapper_position.values():
                current_row = bomb_row + direction[0]
                current_col = bomb_col + direction[1]

                if is_index_in_range(current_row, matrix) and is_index_in_range(current_col, matrix):
                    if matrix[current_row][current_col] > 0:
                        matrix[current_row][current_col] -= bomb_value

            matrix[bomb_row][bomb_col] = 0
            # print(matrix)

alive_cells = []
for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        if matrix[r][c] > 0:
            alive_cells.append(matrix[r][c])

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
for r in matrix:
    print(*r, sep=" ")
