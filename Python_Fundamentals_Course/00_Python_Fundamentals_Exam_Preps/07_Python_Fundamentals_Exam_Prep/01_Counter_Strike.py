# •	On the first line you will receive initial energy – an integer [1-10000].
# •	On the next lines, you will be receiving distance of the enemy – an integer [1-10000]


initial_energy = int(input())
distance_of_the_enemy = input()
current_energy = initial_energy
battles_won = 0
fail = False

while not distance_of_the_enemy == "End of battle":
    distance_of_the_enemy = int(distance_of_the_enemy)
    if current_energy >= distance_of_the_enemy:
        current_energy -= distance_of_the_enemy
        battles_won += 1
        if battles_won % 3 == 0:
            current_energy += battles_won

    else:
        fail = True
        print(f'Not enough energy! Game ends with {battles_won} won battles and {current_energy} energy')
        break

    distance_of_the_enemy = input()

if not fail:
    print(f'Won battles: {battles_won}. Energy left: {current_energy}')
