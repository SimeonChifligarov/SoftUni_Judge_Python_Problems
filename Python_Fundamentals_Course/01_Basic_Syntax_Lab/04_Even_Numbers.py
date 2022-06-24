n = int(input())

are_all_evens = True

for i in range(n):
    number = int(input())
    if not number % 2 == 0:
        print(f'{number} is odd!')
        are_all_evens = False
        break

if are_all_evens:
    print('All numbers are even.')
