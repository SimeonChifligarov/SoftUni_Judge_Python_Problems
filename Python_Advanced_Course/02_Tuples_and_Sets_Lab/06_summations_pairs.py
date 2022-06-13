numbers = [int(el) for el in input().split()]
target_number = int(input())

iterations_done = 0
unique_pairs = set()

for i in range(len(numbers)):
    current_number = numbers[i]
    for j in range(len(numbers) - i - 1):
        iterations_done += 1
        current_second_number = numbers[i + j + 1]
        if current_number + current_second_number == target_number:
            print(f'{current_number} + {current_second_number} = {target_number}')
            current_tuple = (current_number, current_second_number)
            if current_tuple not in unique_pairs or (current_second_number, current_number) not in unique_pairs:
                unique_pairs.add(current_tuple)

print(f'Iterations done: {iterations_done}')
[print(el) for el in unique_pairs]
