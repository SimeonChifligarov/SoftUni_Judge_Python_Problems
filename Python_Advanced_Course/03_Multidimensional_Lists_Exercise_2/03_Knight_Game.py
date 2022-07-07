from pprint import pprint


def are_coords_valid(coord_x, coord_y, mtrx):
    return 0 <= coord_x < len(matrix) and 0 <= coord_y < len(matrix[coord_x])


def kills(king, mtrx):
    kills_count = 0
    for move in MOVES_MAPPER.values():
        potential_pos = (king[0] + move[0]), (king[1] + move[1])
        if are_coords_valid(potential_pos[0], potential_pos[1], mtrx):
            if mtrx[potential_pos[0]][potential_pos[1]] == KNIGHT_SIGN:
                kills_count += 1

    return kills_count


def update_matrix(kngt_to_rmv, mtrx):
    mtrx[kngt_to_rmv[0]][kngt_to_rmv[1]] = EMPTY_SIGN
    return mtrx


MOVES_MAPPER = {
    'LU': (-2, -1),
    'UL': (-1, -2),
    'UR': (-2, 1),
    'RU': (-1, 2),
    'RD': (2, 1),
    'DR': (1, 2),
    'DL': (2, -1),
    'LD': (1, -2),
}

EMPTY_SIGN = '0'
KNIGHT_SIGN = 'K'
removed_knights = 0

matrix_size = int(input())

matrix = []

for _ in range(matrix_size):
    row = list(input())
    matrix.append(row)

# pprint(matrix)

knights_pos = []

for i in range(matrix_size):
    for j in range(matrix_size):
        if matrix[i][j] == KNIGHT_SIGN:
            knights_pos.append((i, j))

# print(kings_pos)


while True:
    max_kills_king = 0
    knight_to_remove = None
    for knight in knights_pos:
        king_kills = kills(knight, matrix)
        if king_kills > max_kills_king:
            max_kills_king = king_kills
            knight_to_remove = knight

    if max_kills_king == 0:
        break

    knights_pos.remove(knight_to_remove)
    removed_knights += 1
    matrix = update_matrix(knight_to_remove, matrix)

print(removed_knights)
