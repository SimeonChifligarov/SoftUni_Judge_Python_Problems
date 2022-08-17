legendary_items = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}

key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}

data = input().split()

is_obtained = False

while not is_obtained:
    for index in range(0, len(data) - 1, 2):
        if not is_obtained:
            quantity = int(data[index])
            material = data[index + 1].lower()

            if material in key_materials:
                key_materials[material] += quantity
                if key_materials[material] >= 250:
                    key_materials[material] -= 250
                    is_obtained = True
                    print(f"{legendary_items[material]} obtained!")
            else:
                if material not in junk:
                    junk[material] = 0
                junk[material] += quantity
    if not is_obtained:
        data = input().split()

# # Then, print the remaining shards, fragments, motes, ordered by quantity in descending order,
# # then by name in ascending order, each on a new line. Finally, print the collected junk items in alphabetical order.
#
# sorted_key_materials = sorted(key_materials.items(), key=lambda kvp: (-kvp[1], kvp[0]))
# for mat, quant in sorted_key_materials:
#     print(f"{mat}: {quant}")
#
# sorted_junks = sorted(junk.items())
# for mat, quant in sorted_junks:
#     print(f"{mat}: {quant}")

for mat, quant in key_materials.items():
    print(f"{mat}: {quant}")

for mat, quant in junk.items():
    print(f"{mat}: {quant}")
