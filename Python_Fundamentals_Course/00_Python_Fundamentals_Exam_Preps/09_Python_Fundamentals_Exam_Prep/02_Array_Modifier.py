# On the first input line you will be given the initial array values separated by a single space.
# On the next lines you will receive commands until you receive the command “end”. The commands are as follow:
# •	“swap {index1} {index2}”
# •	“multiply {index1} {index2}”
# •	“decrease”

integers_as_list = [int(num) for num in input().split()]

command = input()

while not command == "end":
    command = command.split()
    real_command = command[0]
    if real_command == "swap":
        index_one = int(command[1])
        index_two = int(command[2])
        integers_as_list[index_one], integers_as_list[index_two] = integers_as_list[index_two], integers_as_list[
            index_one]
    elif real_command == "multiply":
        index_one = int(command[1])
        index_two = int(command[2])
        integers_as_list[index_one] = integers_as_list[index_one] * integers_as_list[index_two]
    elif real_command == "decrease":
        integers_as_list = [num - 1 for num in integers_as_list]

    command = input()

print(*integers_as_list, sep=", ")
