strings = input().split()

while True:
    command = input()

    if command == '3:1':
        break

    command_tokens = command.split()
    real_command = command_tokens[0]

    if real_command == 'merge':
        start_index = int(command_tokens[1])
        end_index = int(command_tokens[2])
        if start_index < 0:
            start_index = 0
        elif start_index > len(strings) - 1:
            start_index = len(strings) - 1
        if end_index < 0:
            end_index = 0
        elif end_index > len(strings) - 1:
            end_index = len(strings) - 1

        if start_index >= end_index:
            continue

        new_element = ''.join(strings[start_index:end_index + 1])
        strings = strings[:start_index] + [new_element] + strings[end_index + 1:]

    elif real_command == 'divide':
        index = int(command_tokens[1])
        partitions = int(command_tokens[2])

        element = strings[index]
        el_len = len(element) // partitions

        new_element = []
        for _ in range(partitions - 1):
            new_element.append(element[:el_len])
            element = element[el_len:]
        new_element.append(element)

        strings = strings[:index] + new_element + strings[index + 1:]

print(*strings)
