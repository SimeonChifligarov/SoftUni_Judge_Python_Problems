#

number = int(input())

num_as_list = []

for num in range(1, number + 1):
    num_as_string = str(num)
    num_as_list = [int(digit) for digit in num_as_string]
    if sum(num_as_list) == 5 or sum(num_as_list) == 7 or sum(num_as_list) == 11:
        print(f'{num} -> True')
    else:
        print(f'{num} -> False')
