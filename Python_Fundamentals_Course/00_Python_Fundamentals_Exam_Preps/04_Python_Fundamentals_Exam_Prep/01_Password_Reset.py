#

raw_pass = input()
current_pass = raw_pass
command = input()

while not command == "Done":
    command_split = command.split()
    real_command = command_split[0]
    if real_command == "TakeOdd":
        result = ""
        for index_a in range(1, len(current_pass), 2):
            result += current_pass[index_a]
        current_pass = result
        print(current_pass)
    elif real_command == "Cut":
        index = int(command_split[1])
        length = int(command_split[2])
        result = current_pass[:index] + current_pass[index + length:]
        current_pass = result
        print(current_pass)
    elif real_command == "Substitute":
        substring = command_split[1]
        substitute = command_split[2]
        if substring in current_pass:
            current_pass = current_pass.replace(substring, substitute)
            print(current_pass)
        else:
            print("Nothing to replace!")
    command = input()

print(f"Your password is: {current_pass}")
