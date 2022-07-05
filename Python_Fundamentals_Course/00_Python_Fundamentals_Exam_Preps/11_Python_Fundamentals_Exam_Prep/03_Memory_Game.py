# 03. Memory game

list_of_inputs = input().split()

command = input()

number_of_moves = 0
winner = False

while not command == "end":
    number_of_moves += 1
    command = command.split()
    index_one = int(command[0])
    index_two = int(command[1])
    if index_one not in range(len(list_of_inputs)) or index_two not in range(
            len(list_of_inputs)) or index_one == index_two:
        print('Invalid input! Adding additional elements to the board')
        list_of_inputs.insert(int(len(list_of_inputs) / 2), f"-{number_of_moves}a")
        list_of_inputs.insert(int(len(list_of_inputs) / 2), f"-{number_of_moves}a")
    else:
        if list_of_inputs[index_one] == list_of_inputs[index_two]:
            print(f'Congrats! You have found matching elements - {list_of_inputs[index_one]}!')
            list_of_inputs.pop(max(index_one, index_two))
            list_of_inputs.pop(min(index_one, index_two))
            if not len(list_of_inputs):
                winner = True
                print(f'You have won in {number_of_moves} turns!')
                break
        else:
            print(f'Try again!')
    command = input()

if not winner:
    print('Sorry you lose :(')
    print(*list_of_inputs, sep=" ")
