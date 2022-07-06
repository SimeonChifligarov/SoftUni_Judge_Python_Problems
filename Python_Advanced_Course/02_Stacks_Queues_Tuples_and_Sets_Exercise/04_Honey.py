from collections import deque

working_bees = deque([int(el) for el in input().split()])
nectar = deque([int(el) for el in input().split()])
honey_making_process_symbols = deque(input().split())
total_honey_made = 0
current_symbol = None

while working_bees and nectar:
    current_bee = working_bees.popleft()
    current_nectar = nectar.pop()

    while (current_bee > current_nectar) and nectar:
        current_nectar = nectar.pop()

    if honey_making_process_symbols:
        current_symbol = honey_making_process_symbols.popleft()

    if current_bee > current_nectar:
        working_bees.appendleft(current_bee)

    if current_symbol and (current_bee < current_nectar):
        if current_symbol == '+':
            total_honey_made += abs(current_bee + current_nectar)
        elif current_symbol == '-':
            total_honey_made += abs(current_bee - current_nectar)
        elif current_symbol == '*':
            total_honey_made += abs(current_bee * current_nectar)
        elif current_symbol == '/':
            total_honey_made += abs(current_bee / current_nectar)

print(f'Total honey made: {total_honey_made}')
if working_bees:
    print(f'Bees left: {", ".join([str(el) for el in working_bees])}')
if nectar:
    print(f'Nectar left: {", ".join([str(el) for el in nectar])}')
