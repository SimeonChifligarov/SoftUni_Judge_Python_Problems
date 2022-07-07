import math

rows, cols = [int(el) for el in input().split()]

snake = input()

total_squares = rows * cols
num_of_multiplies = math.ceil(total_squares / len(snake))
total_snake = snake * num_of_multiplies

for i in range(rows):
    if i % 2 == 0:
        print(total_snake[:cols])
    else:
        print(total_snake[:cols][::-1])
    total_snake = total_snake[cols:]
