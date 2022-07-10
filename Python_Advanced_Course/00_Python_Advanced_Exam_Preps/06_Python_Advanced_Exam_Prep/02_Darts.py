import math


def is_index_in_range(index, square_matrix_size=7):
    return 0 <= index < square_matrix_size


size_of_square_matrix = 7

players = input().split(", ")

players_and_scores = {player: 501 for player in players}

matrix = []

for _ in range(size_of_square_matrix):
    row = [int(el) if el not in ["D", "T", "B"] else el for el in input().split()]
    matrix.append(row)

# from pprint import pprint
# pprint(matrix)

turn = 0
while True:
    if min(players_and_scores.values()) <= 0:
        break

    turn += 1
    current_player = players[0] if not turn % 2 == 0 else players[1]

    coordinates_info = input()
    row, col = [int(el) for el in coordinates_info[1:-1].split(", ")]

    if is_index_in_range(row) and is_index_in_range(col):
        if matrix[row][col] == "B":
            print(f"{current_player} won the game with {math.ceil(turn / 2)} throws!")
            break
        elif matrix[row][col] not in ["D", "T", "B"]:
            players_and_scores[current_player] -= matrix[row][col]
        elif matrix[row][col] in ["D", "T"]:
            base_score = matrix[row][0] + matrix[row][-1] + matrix[0][col] + matrix[-1][col]
            if matrix[row][col] == "D":
                players_and_scores[current_player] -= base_score * 2
            elif matrix[row][col] == "T":
                players_and_scores[current_player] -= base_score * 3

if min(players_and_scores.values()) <= 0:
    last_player = players[0] if not turn % 2 == 0 else players[1]
    print(f"{last_player} won the game with {math.ceil(turn / 2)} throws!")
