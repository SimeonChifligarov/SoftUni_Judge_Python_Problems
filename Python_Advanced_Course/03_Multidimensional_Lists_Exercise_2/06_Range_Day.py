from pprint import pprint


def check_coords(x, y, mtrx):
    return 0 <= x < len(mtrx) and 0 <= y < len(mtrx[x])


SQUARE_MATRIX_SIZE = 5

MY_SYMBOL = 'A'
TARGET_SYMBOL = 'x'
EMPTY_SYMBOL = '.'

MAPPER_DIRECTION = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

my_position = None
targets_count = 0
targets_shot = 0
targets_shot_positions = []

field = []

for r in range(SQUARE_MATRIX_SIZE):
    row = input().split()
    field.append(row)
    if TARGET_SYMBOL in row:
        targets_count += row.count(TARGET_SYMBOL)
    if MY_SYMBOL in row:
        my_position = (r, row.index(MY_SYMBOL))

# pprint(field)
# print(targets_count)
# print(my_position)

number_of_commands = int(input())

for _ in range(number_of_commands):
    if targets_shot == targets_count:
        break

    command_tokens = input().split()

    real_command = command_tokens[0]
    direction = command_tokens[1]
    if real_command == 'move':  # TODO 'move' as a COMMAND_CONSTANT...
        steps = int(command_tokens[2])
        next_row = my_position[0] + MAPPER_DIRECTION[direction][0] * steps
        next_col = my_position[1] + MAPPER_DIRECTION[direction][1] * steps
        if not check_coords(next_row, next_col, field):
            continue
        if not field[next_row][next_col] == EMPTY_SYMBOL:
            continue

        field[my_position[0]][my_position[1]] = EMPTY_SYMBOL
        my_position = (next_row, next_col)
        field[my_position[0]][my_position[1]] = MY_SYMBOL

    elif real_command == 'shoot':  # TODO ...
        for i in range(SQUARE_MATRIX_SIZE):
            next_row = my_position[0] + MAPPER_DIRECTION[direction][0] * (i + 1)
            next_col = my_position[1] + MAPPER_DIRECTION[direction][1] * (i + 1)

            if not check_coords(next_row, next_col, field):
                break

            if field[next_row][next_col] == TARGET_SYMBOL:
                targets_shot += 1
                targets_shot_positions.append([next_row, next_col])
                field[next_row][next_col] = EMPTY_SYMBOL
                break

if targets_shot == targets_count:
    print(f'Training completed! All {targets_shot} targets hit.')
else:
    print(f'Training not completed! {targets_count - targets_shot} targets left.')

for t in targets_shot_positions:
    print(t)
