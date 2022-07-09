def list_manipulator(list_of_numbers, add_or_remove, beginning_or_end, *args):
    current_list = [num for num in list_of_numbers]
    new_list = []

    if add_or_remove == "add":
        if beginning_or_end == "beginning":
            new_list = list(args) + current_list
        elif beginning_or_end == "end":
            new_list = current_list + list(args)
    elif add_or_remove == "remove":
        if beginning_or_end == "beginning":
            to_be_removed = args[0] if args else 1
            new_list = current_list[to_be_removed:]

        elif beginning_or_end == "end":
            to_be_removed = -args[0] if args else -1
            new_list = current_list[:to_be_removed]

    return new_list


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
