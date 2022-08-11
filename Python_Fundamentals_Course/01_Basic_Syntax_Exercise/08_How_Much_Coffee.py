commands = ['coding', 'dog', 'cat', 'movie']

coffees_needed = 0
while True:
    command = input()

    if command == 'END':
        break

    for possible_command in commands:
        if command == possible_command:
            coffees_needed += 1
            continue
        elif command == possible_command.upper():
            coffees_needed += 2
            continue

if coffees_needed > 5:
    print('You need extra sleep')
else:
    print(coffees_needed)
