def is_position_in_range(row_index, col_index, matrix):
    if 0 <= row_index < len(matrix):
        if 0 <= col_index < len(matrix[row_index]):
            return True
    return False


mapper_movement = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}

matrix_row, matrix_col = [int(el) for el in input().split()]

matrix = []

for r in range(matrix_row):
    row = list(input())
    matrix.append(row)
    if "P" in row:
        player_row = r
        player_col = row.index("P")
        player_position = (player_row, player_col)

# from pprint import pprint
# pprint(matrix)

commands = list(input())

all_bunnies = []
is_winner = False
is_dead = False

for command in commands:
    current_row = player_row + mapper_movement[command][0]
    current_col = player_col + mapper_movement[command][1]

    matrix[player_row][player_col] = "."

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == "B":
                all_bunnies.append((r, c))
    for bunny in all_bunnies:
        for direction in mapper_movement.values():
            new_row = bunny[0] + direction[0]
            new_col = bunny[1] + direction[1]

            if is_position_in_range(new_row, new_col, matrix):
                matrix[new_row][new_col] = "B"

    if not is_position_in_range(current_row, current_col, matrix):
        is_winner = True
        last_player_position = (player_row, player_col)
        break

    else:
        if matrix[current_row][current_col] == "B":
            is_dead = True
            last_player_position = (current_row, current_col)
            break

        else:
            matrix[current_row][current_col] = "P"
            player_row, player_col = current_row, current_col

    # pprint(matrix)

for r in matrix:
    print(*r, sep="")

if is_winner:
    print(f"won: {last_player_position[0]} {last_player_position[1]}")

if is_dead:
    print(f"dead: {last_player_position[0]} {last_player_position[1]}")
