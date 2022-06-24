# The input will be a single string containing the animals separated by comma and a single space ", "

animals_as_string = input().split(", ")
animals_as_string.reverse()

if animals_as_string.index("wolf") == 0:
    print('Please go away and stop eating my sheep')
else:
    print(f'Oi! Sheep number {animals_as_string.index("wolf")}! You are about to be eaten by a wolf!')
