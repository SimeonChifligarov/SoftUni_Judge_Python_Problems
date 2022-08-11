forbidden_symbols = [',', '.', '_']

num_of_string = int(input())

for _ in range(num_of_string):
    string = input()
    for sym in forbidden_symbols:
        if sym in string:
            print(f'{string} is not pure!')
            break
    else:
        print(f'{string} is pure.')
