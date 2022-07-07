from pprint import pprint


def are_coords_valid(x, y, mtrx):
    return 0 <= x < len(mtrx) and 0 <= y < len(mtrx[x])


def are_needed_bags_of_tea_collected(current_bags, needed_bags):
    return current_bags >= needed_bags


field_size = int(input())

ALICE_SYMBOL = 'A'
RABBIT_HOLE_SYMBOL = 'R'
EMPTY_SYMBOL = '.'
PATH_SYMBOL = '*'
NEEDED_BAGS_OF_TEA = 10
SUCCESSFUL_MESSAGE = 'She did it! She went to the party.'
UNSUCCESSFUL_MESSAGE = 'Alice didn\'t make it to the tea party.'

alice_starting_position = None
alice_bags_of_tea = 0

field = []

for i in range(field_size):
    row = [el if el in [ALICE_SYMBOL, RABBIT_HOLE_SYMBOL, EMPTY_SYMBOL] else int(el) for el in input().split()]
    field.append(row)
    if ALICE_SYMBOL in row:
        alice_starting_position = (i, row.index(ALICE_SYMBOL))

# pprint(field)
# print(alice_starting_position)

MAPPER_POS = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

alice_current_position = alice_starting_position
while True:
    current_command = input()
    field[alice_current_position[0]][alice_current_position[1]] = PATH_SYMBOL
    alice_next_row = alice_current_position[0] + MAPPER_POS[current_command][0]
    alice_next_col = alice_current_position[1] + MAPPER_POS[current_command][1]
    if not are_coords_valid(alice_next_row, alice_next_col, field):
        break

    alice_current_position = (alice_next_row, alice_next_col)
    if field[alice_current_position[0]][alice_current_position[1]] == RABBIT_HOLE_SYMBOL:
        field[alice_current_position[0]][alice_current_position[1]] = PATH_SYMBOL
        break

    if field[alice_current_position[0]][alice_current_position[1]] in [EMPTY_SYMBOL, PATH_SYMBOL]:
        continue

    alice_bags_of_tea += field[alice_current_position[0]][alice_current_position[1]]
    if are_needed_bags_of_tea_collected(alice_bags_of_tea, NEEDED_BAGS_OF_TEA):
        field[alice_current_position[0]][alice_current_position[1]] = PATH_SYMBOL
        break

if are_needed_bags_of_tea_collected(alice_bags_of_tea, NEEDED_BAGS_OF_TEA):
    print(SUCCESSFUL_MESSAGE)
else:
    print(UNSUCCESSFUL_MESSAGE)

[print(*r) for r in field]
