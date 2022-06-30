# {dwarfName} <:> {dwarfHatColor} <:> {dwarfPhysics}

data = input()
colors = {}
dwarfs = {}

while not data == "Once upon a time":
    split_data = data.split(" <:> ")
    dwarf_name = split_data[0]
    dwarf_hat_color = split_data[1]
    if dwarf_hat_color not in colors:
        colors[dwarf_hat_color] = 0
    colors[dwarf_hat_color] += 1
    dwarf_physics = int(split_data[2])
    name_plus_color = dwarf_name + dwarf_hat_color
    if name_plus_color not in dwarfs:
        # dwarfs[name_plus_color] = {}
        dwarfs[name_plus_color] = {'name': dwarf_name, 'color': dwarf_hat_color, 'physics': dwarf_physics}

    else:
        if dwarf_physics > dwarfs[name_plus_color]["physics"]:
            dwarfs[name_plus_color]["physics"] = dwarf_physics
            colors[dwarf_hat_color] -= 1
    data = input()

real_dwarfs = list(dwarfs.values())

for curr_dwarf in real_dwarfs:
    for col in colors:
        if col == curr_dwarf["color"]:
            curr_dwarf["samecolor"] = colors[col]

sorted_real_dwarfs = sorted(real_dwarfs, key=lambda x: (-x["physics"], -x["samecolor"]))

for el in sorted_real_dwarfs:
    print(f"({el['color']}) {el['name']} <-> {el['physics']}")
