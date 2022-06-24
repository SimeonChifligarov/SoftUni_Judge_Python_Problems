budget = int(input())
command = input()

is_overdraft = False

while not command == 'End':
    product_price = int(command)
    budget -= product_price
    if budget < 0:
        print('You went in overdraft!')
        is_overdraft = True
        break
    command = input()

if not is_overdraft:
    print('You bought everything needed.')
