# The input will consist of exactly 2 lines:
# •	quantity – integer in range [1…100]
# •	days – integer in range [1…100]

quantity = int(input())
days = int(input())

ORNAMENT_PRICE = 2
TREE_SKIRT_PRICE = 5
TREE_GARLANDS_PRICE = 3
TREE_LIGHTS_PRICE = 15

budget = 0
total_spirits = 0

# Every second day you buy an Ornament Set quantity of times and increase your Christmas spirit by 5.
# Every third day you buy Tree Skirts and Tree Garlands (both quantity of times) and increase your spirit by 13.
# Every fifth day you buy Tree Lights quantity of times and increase your Christmas spirit by 17.
# If you have bought Tree Skirts and Tree Garlands at the same day you additionally increase your spirit by 30.
# Every tenth day you lose 20 spirit, because your cat ruins all tree decorations and you have to rebuild the tree
# and buy one piece of tree skirt, garlands and lights. That is why you are forced to increase the allowed quantity
# with 2 at the beginning of every eleventh day.
# Also if the last day is a tenth day the cat decides to demolish even more and ruins the Christmas turkey and you
# lose additional 30 spirit.
# At the end you must print the total cost and the gained spirit.

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        budget -= ORNAMENT_PRICE * quantity
        total_spirits += 5
    if day % 3 == 0:
        budget -= TREE_SKIRT_PRICE * quantity + TREE_GARLANDS_PRICE * quantity
        total_spirits += 13
    if day % 5 == 0:
        budget -= TREE_LIGHTS_PRICE * quantity
        total_spirits += 17
        if day % 3 == 0:
            total_spirits += 30
    if day % 10 == 0:
        total_spirits -= 20
        budget -= TREE_SKIRT_PRICE + TREE_GARLANDS_PRICE + TREE_LIGHTS_PRICE

if days % 10 == 0:
    total_spirits -= 30

print(f"Total cost: {abs(budget)}")
print(f"Total spirit: {total_spirits}")
