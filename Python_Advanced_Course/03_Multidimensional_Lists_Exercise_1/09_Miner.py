def is_index_in_range(index, square_matrix):
    return 0 <= index < len(square_matrix)


mapper_movement = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

square_matrix_size = int(input())

commands = input().split()

matrix = []

for r in range(square_matrix_size):
    row = input().split()
    matrix.append(row)
    if "s" in row:
        miner_starting_row = r
        miner_starting_col = row.index("s")
        miner_starting_position = (miner_starting_row, miner_starting_col)

total_coals = 0
for row in matrix:
    total_coals += row.count("c")

# from pprint import pprint
# pprint(matrix)

coal_collected = 0

miner_current_row, miner_current_col = miner_starting_row, miner_starting_col
for command in commands:
    current_row, current_col = miner_current_row + mapper_movement[command][0], miner_current_col + \
                               mapper_movement[command][1]
    if is_index_in_range(current_row, matrix) and is_index_in_range(current_col, matrix):
        matrix[miner_current_row][miner_current_col] = "*"
        miner_current_row, miner_current_col = current_row, current_col
        if matrix[miner_current_row][miner_current_col] == "c":
            coal_collected += 1
            if coal_collected == total_coals:
                print(f"You collected all coal! ({miner_current_row}, {miner_current_col})")
                break
        elif matrix[miner_current_row][miner_current_col] == "e":
            print(f"Game over! ({miner_current_row}, {miner_current_col})")
            break

if not matrix[miner_current_row][miner_current_col] == "e" and not coal_collected == total_coals:
    print(f"{total_coals - coal_collected} pieces of coal left. ({miner_current_row}, {miner_current_col})")
