def is_index_in_range(index, square_matrix):
    return 0 <= index < len(square_matrix)


mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

initial_string = input()
current_string = initial_string
size_of_square_matrix = int(input())

matrix = []

for r in range(size_of_square_matrix):
    row = list(input())
    matrix.append(row)
    if "P" in row:
        player_row = r
        player_col = row.index("P")
        player_pos = (player_row, player_col)

# print(matrix)

number_of_moves = int(input())

for _ in range(number_of_moves):
    command = input()
    current_row = player_row + mapper[command][0]
    current_col = player_col + mapper[command][1]

    if is_index_in_range(current_row, matrix) and is_index_in_range(current_col, matrix):
        if not matrix[current_row][current_col] == "-":
            current_string += matrix[current_row][current_col]
        matrix[player_row][player_col] = "-"
        matrix[current_row][current_col] = "P"
        player_row, player_col = current_row, current_col
    else:
        if initial_string:
            current_string = current_string[:-1]
    # from pprint import pprint
    # pprint(matrix)

print(current_string)
for row in matrix:
    print(*row, sep="")
