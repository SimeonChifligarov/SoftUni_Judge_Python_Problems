non_spoken_name = False

while not non_spoken_name:
    name = input()
    if name == 'Voldemort':
        non_spoken_name = True
        print(f'You must not speak of that name!')
        break

    if name == 'Welcome!':
        break

    if len(name) < 5:
        print(f'{name} goes to Gryffindor.')
    elif len(name) == 5:
        print(f'{name} goes to Slytherin.')
    elif len(name) == 6:
        print(f'{name} goes to Ravenclaw.')
    elif len(name) > 6:
        print(f'{name} goes to Hufflepuff.')

if not non_spoken_name:
    print('Welcome to Hogwarts.')
