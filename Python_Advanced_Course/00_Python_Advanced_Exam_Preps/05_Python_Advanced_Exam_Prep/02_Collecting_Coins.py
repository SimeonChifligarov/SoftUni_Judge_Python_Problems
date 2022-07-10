import math

# def is_index_valid(index, square_matrix):
#     return 0 <= index < len(square_matrix)


command_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

size_of_square_matrix = int(input())

matrix = []

player_row = None
player_col = None

for r in range(size_of_square_matrix):
    row = [int(el) if el not in ["P", "X"] else el for el in input().split()]
    matrix.append(row)
    if "P" in row:
        player_row = r
        player_col = row.index("P")
        player_starting_position = (player_row, player_col)

# from pprint import pprint
# pprint(matrix)

coins_collected = 0
players_path = []
players_path.append([player_row, player_col])

while True:
    command = input()
    if command not in command_mapper:
        continue

    current_row = player_row + command_mapper[command][0]
    current_col = player_col + command_mapper[command][1]
    if current_row < 0:
        current_row = len(matrix) - 1
    elif current_row > len(matrix) - 1:
        current_row = 0
    if current_col < 0:
        current_col = len(matrix) - 1
    elif current_col > len(matrix) - 1:
        current_col = 0

    # if is_index_valid(current_row, matrix) and is_index_valid(current_col, matrix):
    if matrix[current_row][current_col] == "X":
        coins_collected = math.floor(coins_collected / 2)
        players_path.append([current_row, current_col])
        break
    else:
        matrix[player_row][player_col] = 0
        coins_collected += matrix[current_row][current_col]

        players_path.append([current_row, current_col])
        player_row, player_col = current_row, current_col
        player_position = (player_row, player_col)

        if coins_collected >= 100:
            break

    # else:
    #     coins_collected = math.floor(coins_collected / 2)
    #     break

if coins_collected >= 100:
    print(f"You won! You've collected {math.floor(coins_collected)} coins.")
else:
    print(f"Game over! You've collected {math.floor(coins_collected)} coins.")

print("Your path:")
for location in players_path:
    print(location)
