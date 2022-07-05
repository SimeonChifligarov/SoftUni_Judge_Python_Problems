#

concealed_message = input()

current_message = concealed_message
command = input()

while not command == "Reveal":
    split_command = command.split(":|:")
    real_command = split_command[0]
    if real_command == "InsertSpace":
        index_ins = int(split_command[1])
        current_message = current_message[:index_ins] + " " + current_message[index_ins:]
        print(current_message)
    elif real_command == "Reverse":
        substring = split_command[1]
        if substring in current_message:
            current_message = current_message.replace(substring, "", 1)
            current_message = current_message + substring[::-1]
            print(current_message)
        else:
            print("error")
    elif real_command == "ChangeAll":
        substring_change = split_command[1]
        replacement = split_command[2]
        current_message = current_message.replace(substring_change, replacement)
        print(current_message)

    command = input()

print(f"You have a new text message: {current_message}")
