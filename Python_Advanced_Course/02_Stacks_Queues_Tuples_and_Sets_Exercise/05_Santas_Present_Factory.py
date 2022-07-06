from collections import deque

materials = deque([int(el) for el in input().split()])
magic_levels = deque([int(el) for el in input().split()])

magic_needed_present = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle',
}

presents_made = {
    'Doll': 0,
    'Wooden train': 0,
    'Teddy bear': 0,
    'Bicycle': 0,
}

while materials and magic_levels:
    current_material = materials[-1]
    current_magic = magic_levels[0]

    result = current_material * current_magic

    if result in magic_needed_present:
        presents_made[magic_needed_present[result]] += 1
        materials.pop()
        magic_levels.popleft()

    elif result < 0:
        new_result = current_material + current_magic
        materials.pop()
        magic_levels.popleft()
        materials.append(new_result)
    elif result > 0:
        magic_levels.popleft()
        materials[-1] += 15
    elif result == 0:
        if current_material == 0:
            materials.pop()
        if current_magic == 0:
            magic_levels.popleft()

is_task_done = (presents_made['Doll'] > 0 and presents_made['Wooden train'] > 0) or (
        presents_made['Teddy bear'] > 0 and presents_made['Bicycle'] > 0)

if is_task_done:
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if materials:
    print(f'Materials left: {", ".join([str(el) for el in list(materials)[::-1]])}')
if magic_levels:
    print(f'Magic left: {", ".join([str(el) for el in magic_levels])}')

for k, v in sorted(presents_made.items(), key=lambda item: item[0]):
    if not v == 0:
        print(f'{k}: {v}')
