# neighborhood

neighborhood = [int(house) for house in input().split("@")]

success = 0
jump_command = input()
current_position = 0
while not jump_command == "Love!":
    jump_command = jump_command.split()
    jump_length = int(jump_command[-1])
    current_position += jump_length
    if current_position + 1 > len(neighborhood):
        current_position = 0
        neighborhood[0] -= 2
        if neighborhood[0] == 0:
            print('Place 0 has Valentine\'s day.')
            success += 1
        elif neighborhood[0] < 0:
            print('Place 0 already had Valentine\'s day.')
    else:
        neighborhood[current_position] -= 2
        if neighborhood[current_position] == 0:
            print(f'Place {current_position} has Valentine\'s day.')
            success += 1
        elif neighborhood[current_position] < 0:
            print(f'Place {current_position} already had Valentine\'s day.')

    jump_command = input()

print(f'Cupid\'s last position was {current_position}.')
if success == len(neighborhood):
    print('Mission was successful.')
else:
    print(f'Cupid has failed {len(neighborhood) - success} places.')
