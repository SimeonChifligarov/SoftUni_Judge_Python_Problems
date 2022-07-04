# •	The first line of the input will be string and it will consist of letters and numbers only.
# •	After the first line, until the "Generate" command is given, you will be receiving strings.

raw_key = input()

command = input()

while not command == "Generate":
    split_command = command.split(">>>")
    real_command = split_command[0]
    if real_command == "Contains":
        substring = split_command[1]
        if substring in raw_key:
            print(f"{raw_key} contains {substring}")
        else:
            print("Substring not found!")
    elif real_command == "Flip":
        upper_or_lower = split_command[1]
        start_index = int(split_command[2])
        end_index = int(split_command[3])
        if upper_or_lower == "Upper":
            for index_a in range(start_index, end_index):
                char = raw_key[index_a]
                raw_key = raw_key[:index_a] + char.upper() + raw_key[index_a + 1:]
        elif upper_or_lower == "Lower":
            for index_a in range(start_index, end_index):
                char = raw_key[index_a]
                raw_key = raw_key[:index_a] + char.lower() + raw_key[index_a + 1:]
        print(raw_key)
    elif real_command == "Slice":
        start_index_b = int(split_command[1])
        end_index_b = int(split_command[2])
        raw_key = raw_key[:start_index_b] + raw_key[end_index_b:]
        print(raw_key)

    command = input()
print(f"Your activation key is: {raw_key}")
