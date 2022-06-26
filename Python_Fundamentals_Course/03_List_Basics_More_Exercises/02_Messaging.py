numbers_input_as_list = [int(el) for el in input().split()]
# print(numbers_input_as_list)
starting_message = input()

starting_message_copy = starting_message
result = []

indexes_of_interest = []
for num in numbers_input_as_list:
    current_list = list(str(num))
    current_index = sum([int(el) for el in current_list])
    # print(current_index)
    indexes_of_interest.append(current_index)

for idx in indexes_of_interest:
    real_idx = idx % len(starting_message_copy)
    current_char = starting_message_copy[real_idx]
    # print(current_char)
    result.append(current_char)
    starting_message_copy = starting_message_copy[:real_idx] + starting_message_copy[real_idx + 1:]

print(''.join(result))
