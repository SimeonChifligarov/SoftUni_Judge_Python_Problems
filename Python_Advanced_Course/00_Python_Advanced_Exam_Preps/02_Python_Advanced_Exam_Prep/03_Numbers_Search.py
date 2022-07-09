def numbers_searching(*args):
    duplicate_numbers = []
    for num in args:
        if args.count(num) > 1:
            duplicate_numbers.append(num)
    duplicate_numbers = sorted(list(set(duplicate_numbers)))
    missing_value = max([num for num in range(min(args), max(args)) if num not in args])

    return [missing_value, duplicate_numbers]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
