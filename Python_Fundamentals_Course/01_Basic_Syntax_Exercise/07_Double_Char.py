while True:
    string = input()
    if string == 'End':
        break

    if string == 'SoftUni':
        continue

    double_char_list = []
    for char in string:
        double_char_list.append(f'{char}{char}')
    print(''.join(double_char_list))
