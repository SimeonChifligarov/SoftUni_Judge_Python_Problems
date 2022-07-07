from pprint import pprint


def are_coords_valid(x, y, mtrx):
    return 0 <= x < len(mtrx) and 0 <= y < len(mtrx[x])


count_of_presents = int(input())
size_of_square_field = int(input())

SANTA_SYMBOL = 'S'
NAUGHTY_KID_SYMBOL = 'X'
NICE_KID_SYMBOL = 'V'
COOKIE_SYMBOL = 'C'
EMPTY_SYMBOL = '-'
END_COMMAND = 'Christmas morning'

MAPPER_DIRECTION = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

santa_position = None
nice_kids_count = 0
nice_kids_presents = 0

field = []

for r in range(size_of_square_field):
    row = input().split()
    field.append(row)
    if SANTA_SYMBOL in row:
        santa_position = (r, row.index(SANTA_SYMBOL))
    if NICE_KID_SYMBOL in row:
        nice_kids_count += row.count(NICE_KID_SYMBOL)

# pprint(field)
# print(nice_kids_count)

while True:
    if count_of_presents == 0:
        break
    command = input()

    if command == END_COMMAND:
        break

    next_row = santa_position[0] + MAPPER_DIRECTION[command][0]
    next_col = santa_position[1] + MAPPER_DIRECTION[command][1]
    if not are_coords_valid(next_row, next_col, field):
        break

    field[santa_position[0]][santa_position[1]] = EMPTY_SYMBOL
    santa_position = (next_row, next_col)
    current_cell = field[santa_position[0]][santa_position[1]]

    if current_cell == EMPTY_SYMBOL:
        current_cell = SANTA_SYMBOL

    elif current_cell == NICE_KID_SYMBOL:
        if count_of_presents == 0:
            break
        count_of_presents -= 1
        nice_kids_presents += 1

    elif current_cell == NAUGHTY_KID_SYMBOL:
        continue

    elif current_cell == COOKIE_SYMBOL:
        for pos, move in MAPPER_DIRECTION.items():
            around_row = santa_position[0] + move[0]
            around_col = santa_position[1] + move[1]
            if not are_coords_valid(around_row, around_col, field):
                continue

            if field[around_row][around_col] == NICE_KID_SYMBOL:
                if count_of_presents == 0:
                    break
                count_of_presents -= 1
                nice_kids_presents += 1
                field[around_row][around_col] = EMPTY_SYMBOL
            elif field[around_row][around_col] == NAUGHTY_KID_SYMBOL:
                if count_of_presents == 0:
                    break
                count_of_presents -= 1
                field[around_row][around_col] = EMPTY_SYMBOL

    field[santa_position[0]][santa_position[1]] = SANTA_SYMBOL

if count_of_presents == 0 and (nice_kids_presents < nice_kids_count):
    print('Santa ran out of presents!')

[print(*r) for r in field]

if nice_kids_presents == nice_kids_count:
    print(f'Good job, Santa! {nice_kids_presents} happy nice kid/s.')
else:
    print(f'No presents for {nice_kids_count - nice_kids_presents} nice kid/s.')
