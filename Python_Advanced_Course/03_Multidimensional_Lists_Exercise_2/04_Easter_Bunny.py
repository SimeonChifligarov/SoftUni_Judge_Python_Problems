from pprint import pprint


def is_coords_valid(x, y, mtrx):
    return 0 <= x < len(mtrx) and 0 <= y < len(mtrx[x])


size_of_field = int(input())

field = []
BUNNY_SYMBOL = 'B'
TRAP_SYMBOL = 'X'

# SOLUTION No1
starting_bunny_position = None
max_eggs_collected = 0
max_eggs_movement_position = None
max_eggs_track = []

POSITION_MAPPERS = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for i in range(size_of_field):
    row = [el if el in [BUNNY_SYMBOL, TRAP_SYMBOL] else int(el) for el in input().split()]
    field.append(row)
    if BUNNY_SYMBOL in row:
        starting_bunny_position = (i, row.index(BUNNY_SYMBOL))

# pprint(field)
# print(bunny_position)


for pos, move in POSITION_MAPPERS.items():
    current_eggs = 0
    current_eggs_track = []
    bunny_position = starting_bunny_position
    next_pos = (bunny_position[0] + move[0]), (bunny_position[1] + move[1])
    while is_coords_valid(next_pos[0], next_pos[1], field):
        if field[next_pos[0]][next_pos[1]] == TRAP_SYMBOL:
            break

        current_eggs += field[next_pos[0]][next_pos[1]]
        # if not field[next_pos[0]][next_pos[1]] == 0:
        #     current_eggs_track.append([next_pos[0], next_pos[1]])
        current_eggs_track.append([next_pos[0], next_pos[1]])
        next_pos = (next_pos[0] + move[0]), (next_pos[1] + move[1])

    if current_eggs >= max_eggs_collected:
        max_eggs_collected = current_eggs
        max_eggs_movement_position = pos
        max_eggs_track = current_eggs_track

result = []
result.append(max_eggs_movement_position)
# result.extend([str(el) for el in max_eggs_track])
for tr in max_eggs_track:
    result.append(tr)
result.append(max_eggs_collected)

# print(result)

for r in result:
    if r is not None:
        print(r)

# # Solution No2
# for i in range(size_of_field):
#     row = [el if el in [BUNNY_SYMBOL, TRAP_SYMBOL] else int(el) for el in input().split()]
#     field.append(row)
#     if BUNNY_SYMBOL in row:
#         starting_bunny_position = (i, row.index(BUNNY_SYMBOL))
#
# right_result = 0
# right_moves = 0
# left_result = 0
# left_moves = 0
# up_result = 0
# up_moves = 0
# down_result = 0
# down_moves = 0
#
# bunny_row = field[starting_bunny_position[0]]
# bunny_col = []
# for r in field:
#     bunny_col.append(r[starting_bunny_position[1]])
#
# # print(bunny_col)
#
# for el in bunny_row[::-1]:
#     if el == TRAP_SYMBOL:
#         right_result = 0
#         right_moves = 0
#     elif el == BUNNY_SYMBOL:
#         break
#     else:
#         right_result += el
#         right_moves += 1
#
# # print(right_result)
#
# for el in bunny_row:
#     if el == TRAP_SYMBOL:
#         left_result = 0
#         left_moves = 0
#     elif el == BUNNY_SYMBOL:
#         break
#     else:
#         left_result += el
#         left_moves += 1
#
# # print(left_result)
#
# for el in bunny_col:
#     if el == TRAP_SYMBOL:
#         up_result = 0
#         up_moves = 0
#     elif el == BUNNY_SYMBOL:
#         break
#     else:
#         up_result += el
#         up_moves += 1
#
# # print(up_result)
#
# for el in bunny_col[::-1]:
#     if el == TRAP_SYMBOL:
#         down_result = 0
#         down_moves = 0
#     elif el == BUNNY_SYMBOL:
#         break
#     else:
#         down_result += el
#         down_moves += 1
#
# # print(down_result)
#
# max_result = max(up_result, down_result, left_result, right_result)
# max_result_direction = None
# max_result_path = []
# if max_result == up_result:
#     max_result_direction = 'up'
#     for i in range(up_moves):
#         max_result_path.append(f'[{starting_bunny_position[0] - i - 1}, {starting_bunny_position[1]}]')
# elif max_result == down_result:
#     max_result_direction = 'down'
#     for i in range(down_moves):
#         max_result_path.append(f'[{starting_bunny_position[0] + i + 1}, {starting_bunny_position[1]}]')
# elif max_result == left_result:
#     max_result_direction = 'left'
#     for i in range(left_moves):
#         max_result_path.append(f'[{starting_bunny_position[0]}, {starting_bunny_position[1] - i - 1}]')
# elif max_result == right_result:
#     max_result_direction = 'right'
#     for i in range(right_moves):
#         max_result_path.append(f'[{starting_bunny_position[0]}, {starting_bunny_position[1] + i + 1}]')
#
# MOVEMENT_MAPPER = {
#     'up': (-1, 0),
#     'down': (1, 0),
#     'left': (0, -1),
#     'right': (0, 1),
# }
#
# if max_result > 0:
#     print(max_result_direction)
#     print('\n'.join(max_result_path))
#     print(max_result)
