from collections import deque

cups_capacity = deque([int(el) for el in input().split()])
bottles_with_water = [int(el) for el in input().split()]

wasted_water = 0

while cups_capacity and bottles_with_water:
    current_cup = cups_capacity.popleft()
    current_bottle = bottles_with_water.pop()

    if current_cup <= current_bottle:
        wasted_water += current_bottle - current_cup

    else:
        current_cup -= current_bottle
        cups_capacity.appendleft(current_cup)

if bottles_with_water:
    print(f"Bottles: {' '.join([str(el) for el in bottles_with_water[::-1]])}")
elif cups_capacity:
    print(f"Cups: {' '.join([str(el) for el in cups_capacity])}")

print(f"Wasted litters of water: {wasted_water}")
