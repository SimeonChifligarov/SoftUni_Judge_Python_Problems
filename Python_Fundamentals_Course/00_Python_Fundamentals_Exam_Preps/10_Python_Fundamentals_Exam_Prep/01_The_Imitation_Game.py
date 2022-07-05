#

encrypted_message = input()
current_message = encrypted_message
command = input()

while not command == "Decode":
    split_command = command.split("|")
    real_command = split_command[0]
    if real_command == "Move":
        num_of_letters = int(split_command[1])
        current_message = current_message[num_of_letters:] + current_message[:num_of_letters]
    elif real_command == "Insert":
        index_ins = int(split_command[1])
        value = split_command[2]
        current_message = current_message[:index_ins] + value + current_message[index_ins:]
    elif real_command == "ChangeAll":
        substring = split_command[1]
        replacement = split_command[2]
        current_message = current_message.replace(substring, replacement)
    command = input()

print(f"The decrypted message is: {current_message}")
