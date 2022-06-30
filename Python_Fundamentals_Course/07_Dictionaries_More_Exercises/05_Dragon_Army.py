# •	On the first line, you are given number N -> the number of dragons to follow
# •	On the next N lines, you are given input in the above described format.
#   There will be single space separating each element.

number_of_dragons = int(input())
dragon_types = {}

for _ in range(number_of_dragons):
    split_data = input().split()

    # format {type} {name} {damage} {health} {armor}.

    dr_type = split_data[0]
    name = split_data[1]
    damage = 45
    if not split_data[2] == "null":
        damage = int(split_data[2])
    health = 250
    if not split_data[3] == "null":
        health = int(split_data[3])
    armor = 10
    if not split_data[4] == "null":
        armor = int(split_data[4])

    if dr_type not in dragon_types:
        dragon_types[dr_type] = {}
    if name not in dragon_types[dr_type]:
        dragon_types[dr_type][name] = {}
    dragon_types[dr_type][name] = {'damage': damage, 'health': health, 'armor': armor}

for dragon_type, dragon in dragon_types.items():
    stats = dragon.values()
    dmg = 0
    hlth = 0
    arm = 0
    for dr in stats:
        dmg += dr['damage']
        hlth += dr['health']
        arm += dr['armor']
    print(f"{dragon_type}::({dmg / len(stats) :.2f}/{hlth / len(stats) :.2f}/{arm / len(stats) :.2f})")
    for nm, stz in sorted(dragon.items()):
        print(f"-{nm} -> damage: {stz['damage']}, health: {stz['health']}, armor: {stz['armor']}")
