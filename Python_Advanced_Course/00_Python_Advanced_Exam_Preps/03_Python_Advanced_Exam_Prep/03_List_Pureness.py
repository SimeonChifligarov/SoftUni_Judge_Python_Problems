from collections import deque


def best_list_pureness(list_of_numbers, k):
    new_deque = deque(list_of_numbers)

    number_of_rotations = k + 1
    if k > len(list_of_numbers):
        number_of_rotations = len(list_of_numbers) + 1

    highest_pureness = 0
    best_rotation = 0

    for rotation in range(number_of_rotations):
        current_pureness = 0
        for index, number in enumerate(new_deque):
            current_pureness += index * number

        if current_pureness > highest_pureness:
            highest_pureness = current_pureness
            best_rotation = rotation

        new_deque.rotate()

    return f"Best pureness {highest_pureness} after {best_rotation} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
