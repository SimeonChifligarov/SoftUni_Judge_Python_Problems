fires_cells = input().split('#')
water_amount = int(input())
effort = 0
total_fire = 0
condition = False

print('Cells:')
for current_fire in fires_cells:
    fire_info = current_fire.split(' = ')
    type_of_fire = fire_info[0]
    value_fire = int(fire_info[1])
    condition = False

    if type_of_fire == 'High':
        if 81 <= value_fire <= 125:
            condition = True

    elif type_of_fire == 'Medium':
        if 51 <= value_fire <= 80:
            condition = True
    elif type_of_fire == 'Low':
        if 1 <= value_fire <= 50:
            condition = True
    if condition:
        if water_amount >= value_fire:
            water_amount -= value_fire
            effort += value_fire * 0.25
            total_fire += value_fire
            print(f' - {value_fire}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')
