# •	On the 1st line you are going to receive the items with their prices
# in the format described above – real numbers in the range [0.00……1000.00]
# •	On the 2nd line, you are going to be given the budget – a real number in the range [0.0….1000.0]

# Clothes->43.30|Shoes->25.25|Clothes->36.52|Clothes->20.90|Accessories->15.60

list_of_items = input().split("|")
budget = float(input())
item_type = []
potential_items = []
buyed_items = []
for item in list_of_items:
    item_type.append(item.split("->"))
for item in item_type:
    if item[0] == "Clothes" and float(item[1]) <= 50:
        potential_items.append(float(item[1]))
    elif item[0] == "Shoes" and float(item[1]) <= 35:
        potential_items.append(float(item[1]))
    elif item[0] == "Accessories" and float(item[1]) <= 20.50:
        potential_items.append(float(item[1]))
spended = 0
for item in potential_items:
    if item <= budget:
        budget -= item
        spended += item
        buyed_items.append(str(item))
income = 0
for price in buyed_items:
    money = float(price) * 1.40
    print(f'{money:.2f}', end=' ')
    income += money
print()
print(f'Profit: {income - spended:.2f}')
if budget + income >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')
