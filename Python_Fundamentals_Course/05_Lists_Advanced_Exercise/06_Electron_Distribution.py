# Maximum number of electrons in a shell is distributed with a rule of 2n^2

num_of_electrons = int(input())
remaining_electrons = num_of_electrons
electron_distribution = []
level = 1
electron_for_level = 2 * level ** 2
while remaining_electrons > electron_for_level:
    remaining_electrons -= electron_for_level
    electron_distribution.append(electron_for_level)
    level += 1
    electron_for_level = 2 * level ** 2
else:
    electron_distribution.append(remaining_electrons)

print(electron_distribution)
