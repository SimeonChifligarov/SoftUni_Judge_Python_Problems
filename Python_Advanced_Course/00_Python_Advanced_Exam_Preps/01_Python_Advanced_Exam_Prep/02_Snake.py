def is_index_in_range(index, square_matrix):
    return 0 <= index < len(square_matrix)


SNAKE_SYMBOL = "S"

commands = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

size_of_square_matrix = int(input())

matrix = []

for r in range(size_of_square_matrix):
    row = list(input())
    matrix.append(row)
    if SNAKE_SYMBOL in row:
        snake_row = r
        snake_col = row.index(SNAKE_SYMBOL)
        snake_position = (snake_row, snake_col)

# from pprint import pprint
# pprint(matrix)
#
# print(snake_position)

food_eaten = 0

while food_eaten < 10:
    command = input()
    position_deltas = commands[command]
    new_pos_row = snake_position[0] + position_deltas[0]
    new_pos_col = snake_position[1] + position_deltas[1]
    if is_index_in_range(new_pos_row, matrix) and is_index_in_range(new_pos_col, matrix):
        matrix[snake_position[0]][snake_position[1]] = "."
        if matrix[new_pos_row][new_pos_col] == "*":
            food_eaten += 1
            if food_eaten >= 10:
                print("You won! You fed the snake.")
        if matrix[new_pos_row][new_pos_col] == "B":
            matrix[new_pos_row][new_pos_col] = "."
            for r in range(len(matrix)):
                for c in range(len(matrix[r])):
                    if matrix[r][c] == "B":
                        matrix[r][c] = SNAKE_SYMBOL
                        snake_position = (r, c)
        else:
            matrix[new_pos_row][new_pos_col] = SNAKE_SYMBOL
            snake_position = (new_pos_row, new_pos_col)
        # pprint(matrix)
    else:
        matrix[snake_position[0]][snake_position[1]] = "."
        print("Game over!")
        break

print(f"Food eaten: {food_eaten}")
for row in matrix:
    print(*row, sep="")
