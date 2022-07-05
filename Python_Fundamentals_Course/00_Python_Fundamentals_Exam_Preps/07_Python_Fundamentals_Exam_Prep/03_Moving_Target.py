# On the first line, you will receive a sequence of targets with their integer values, split by a single space. Then, you will start receiving commands for manipulating the targets, until the "End" command.

sequence_of_targets = [int(targ) for targ in input().split()]
commands_as_string = input()

while not commands_as_string == "End":
    commands_as_string = commands_as_string.split()
    command = commands_as_string[0]
    index = int(commands_as_string[1])
    value = int(commands_as_string[2])
    if command == "Shoot":
        if index in range(len(sequence_of_targets)):
            sequence_of_targets[index] -= value
            if sequence_of_targets[index] <= 0:
                sequence_of_targets.pop(index)
    elif command == "Add":
        if index in range(len(sequence_of_targets)):
            sequence_of_targets.insert(index, value)
        else:
            print('Invalid placement!')
    elif command == "Strike":
        if index in range(value, len(sequence_of_targets) - value):
            del sequence_of_targets[index - value: index + value + 1]
        else:
            print('Strike missed!')
    commands_as_string = input()

print(*sequence_of_targets, sep="|")
