def fill_the_box(*args):
    args_as_list = list(args)
    box_height = args_as_list[0]
    box_length = args_as_list[1]
    box_width = args_as_list[2]

    box_capacity = box_height * box_length * box_width
    box_capacity_left = box_capacity
    unboxed_cubes = 0

    for current_box in args_as_list[3:]:
        if current_box == 'Finish':
            break

        if box_capacity_left == 0:
            unboxed_cubes += current_box
        elif box_capacity_left < current_box:
            unboxed_cubes += current_box - box_capacity_left
            box_capacity_left = 0
        else:
            box_capacity_left -= current_box

    if box_capacity_left > 0:
        return f'There is free space in the box. You could put {box_capacity_left} more cubes.'
    else:
        return f'No more free space! You have {unboxed_cubes} more cubes.'

# print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
# print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
# print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
