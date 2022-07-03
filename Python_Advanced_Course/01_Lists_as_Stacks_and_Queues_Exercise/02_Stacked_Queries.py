current_stack = []

number_of_commands = int(input())

for _ in range(number_of_commands):
    current_command = [int(el) for el in input().split()]
    real_command = current_command[0]
    if real_command == 1:
        current_number = current_command[1]
        current_stack.append(current_number)
    elif real_command == 2:
        if current_stack:
            current_stack.pop()
    elif real_command == 3:
        if current_stack:
            print(max(current_stack))
    elif real_command == 4:
        if current_stack:
            print(min(current_stack))

reversed_stack = reversed(current_stack)

print(", ".join([str(el) for el in reversed_stack]))
