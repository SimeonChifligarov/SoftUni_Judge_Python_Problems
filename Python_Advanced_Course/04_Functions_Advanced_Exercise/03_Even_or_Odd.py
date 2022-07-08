def even_odd(*args):
    command = args[-1]
    numbers_as_list = list(args[:-1])
    result = None
    if command == "even":
        result = [num for num in numbers_as_list if num % 2 == 0]
    elif command == "odd":
        result = [num for num in numbers_as_list if not num % 2 == 0]

    return result

#
# print(even_odd(1, 2, 3, 4, 5, 6, "even"))
# print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
#
