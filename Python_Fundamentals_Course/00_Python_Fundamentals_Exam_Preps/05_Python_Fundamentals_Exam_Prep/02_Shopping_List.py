# You will receive an initial list with groceries separated by "!".
# After that you will be receiving 4 types of commands, until you receive "Go Shopping!"

initial_list_of_groceries = input().split("!")

command_as_couple = input()

while not command_as_couple == "Go Shopping!":
    command_split = command_as_couple.split()
    command = command_split[0]

    if command == "Urgent":
        grocery = command_split[1]
        if grocery not in initial_list_of_groceries:
            initial_list_of_groceries.insert(0, grocery)
    elif command == "Unnecessary":
        grocery = command_split[1]
        if grocery in initial_list_of_groceries:
            initial_list_of_groceries.remove(grocery)
    elif command == "Correct":
        old_grocery = command_split[1]
        new_grocery = command_split[2]
        if old_grocery in initial_list_of_groceries:
            initial_list_of_groceries[initial_list_of_groceries.index(old_grocery)] = new_grocery
    elif command == "Rearrange":
        grocery = command_split[1]
        if grocery in initial_list_of_groceries:
            initial_list_of_groceries.remove(grocery)
            initial_list_of_groceries.append(grocery)

    command_as_couple = input()
final_result = ", ".join(initial_list_of_groceries)
print(final_result)
