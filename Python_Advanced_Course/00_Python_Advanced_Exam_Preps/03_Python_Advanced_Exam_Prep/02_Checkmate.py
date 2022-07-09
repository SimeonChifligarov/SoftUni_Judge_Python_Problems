def is_index_in_range(index, square_matrix_size=8):
    return 0 <= index < square_matrix_size


mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "ul": (-1, -1),
    "ur": (-1, 1),
    "dl": (1, -1),
    "dr": (1, 1),
}

matrix = []

for r in range(8):
    row = input().split()
    matrix.append(row)
    if "K" in row:
        king_row = r
        king_col = row.index("K")
        king_position = (king_row, king_col)

# from pprint import pprint
# pprint(matrix)

queens_of_interest = []

for move in mapper.values():
    current_k_row = king_row
    current_k_col = king_col
    for _ in range(len(matrix)):
        current_k_row += move[0]
        current_k_col += move[1]
        if is_index_in_range(current_k_row) and is_index_in_range(current_k_col):
            if matrix[current_k_row][current_k_col] == "Q":
                queen_position = [current_k_row, current_k_col]
                queens_of_interest.append(queen_position)
                break

if queens_of_interest:
    print(*queens_of_interest, sep='\n')
else:
    print("The king is safe!")
