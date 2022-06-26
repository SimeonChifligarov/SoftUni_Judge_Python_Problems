list_of_numbers = [int(el) for el in input().split()]

while True:
    command = input()

    if command == 'end':
        break

    tokens = command.split()
    real_command = tokens.pop(0)

    if real_command == 'exchange':
        index = int(tokens[0])
        if index < 0 or index >= len(list_of_numbers):
            print('Invalid index')
        else:
            list_of_numbers = list_of_numbers[index + 1:] + list_of_numbers[:index + 1]

    elif real_command == 'max':
        even_or_odd = tokens[0]

        if even_or_odd == 'even':
            even_numbers = [n for n in list_of_numbers if n % 2 == 0]
            if not even_numbers:
                print('No matches')
            else:
                max_even_number = max(even_numbers)
                for i in range(len(list_of_numbers)):
                    if list_of_numbers[i] == max_even_number:
                        rightmost_index = i
                print(rightmost_index)

        elif even_or_odd == 'odd':
            odd_numbers = [n for n in list_of_numbers if not n % 2 == 0]
            if not odd_numbers:
                print('No matches')
            else:
                max_odd_number = max(odd_numbers)
            for i in range(len(list_of_numbers)):
                if list_of_numbers[i] == max_odd_number:
                    rightmost_index = i
            print(rightmost_index)

    elif real_command == 'min':
        even_or_odd = tokens[0]

        if even_or_odd == 'even':
            even_numbers = [n for n in list_of_numbers if n % 2 == 0]
            if not even_numbers:
                print('No matches')
            else:
                min_even_number = min(even_numbers)
                for i in range(len(list_of_numbers)):
                    if list_of_numbers[i] == min_even_number:
                        rightmost_index = i
                print(rightmost_index)

        elif even_or_odd == 'odd':
            odd_numbers = [n for n in list_of_numbers if not n % 2 == 0]
            if not odd_numbers:
                print('No matches')
            else:
                min_odd_number = min(odd_numbers)
            for i in range(len(list_of_numbers)):
                if list_of_numbers[i] == min_odd_number:
                    rightmost_index = i
            print(rightmost_index)

    elif real_command == 'first':
        count = int(tokens[0])
        even_or_odd = tokens[1]

        if count > len(list_of_numbers):
            print('Invalid count')

        else:
            if even_or_odd == 'even':
                even_numbers = [n for n in list_of_numbers if n % 2 == 0]
                real_count = min([count, len(even_numbers)])
                print(even_numbers[:real_count])
            elif even_or_odd == 'odd':
                odd_numbers = [n for n in list_of_numbers if not n % 2 == 0]
                real_count = min([count, len(odd_numbers)])
                print(odd_numbers[:real_count])

    elif real_command == 'last':
        count = int(tokens[0])
        even_or_odd = tokens[1]

        if count > len(list_of_numbers):
            print('Invalid count')

        else:
            if even_or_odd == 'even':
                even_numbers = [n for n in list_of_numbers if n % 2 == 0]
                real_count = min([count, len(even_numbers)])
                print(even_numbers[::-1][:real_count][::-1])
            elif even_or_odd == 'odd':
                odd_numbers = [n for n in list_of_numbers if not n % 2 == 0]
                real_count = min([count, len(odd_numbers)])
                print(odd_numbers[::-1][:real_count][::-1])

print(list_of_numbers)
