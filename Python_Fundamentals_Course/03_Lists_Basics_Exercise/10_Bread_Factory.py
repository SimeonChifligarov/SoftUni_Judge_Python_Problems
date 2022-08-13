events = input().split('|')

energy = 100
coins = 100
completed = True

for event in events:
    args = event.split('-')

    name = args[0]
    number = int(args[1])

    if name == 'rest':
        gained_energy = 0

        if energy + number <= 100:
            gained_energy = number
            energy += number
        else:
            gained_energy = 100 - energy
            energy = 100
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {energy}.')
    elif name == 'order':
        if energy < 30:
            energy += 50
            print('You had to rest!')
            continue

        energy -= 30
        coins += number
        print(f'You earned {number} coins.')
    else:
        if coins < number:
            print(f"Closed! Cannot afford {name}.")
            completed = False
            break

        coins -= number
        print(f'You bought {name}.')

if completed:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f"Energy: {energy}")
