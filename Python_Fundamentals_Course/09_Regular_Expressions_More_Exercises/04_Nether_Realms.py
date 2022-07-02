import re

all_demons = [el.strip() for el in input().split(",")]
all_demons_dict = []

for demon in all_demons:
    health = 0
    damage = 0
    health_pattern = r"[^0-9\+\*\.\/-]+"
    health_str = "".join(re.findall(health_pattern, demon))
    damage_pattern = r"-?\d+(\.\d+)?"
    damage_str = [float(el.group()) for el in re.finditer(damage_pattern, demon)]

    for char in health_str:
        health += ord(char)

    damage = sum(damage_str)
    if demon.count('*'):
        damage *= 2 ** demon.count("*")
    if demon.count("/"):
        damage /= 2 ** demon.count("/")

    demon_d = {'name': demon, 'health': health, 'damage': damage}
    all_demons_dict.append(demon_d)

sorted_demons = sorted(all_demons_dict, key=lambda x: x['name'])
if sorted_demons:
    for dem in sorted_demons:
        print(f"{dem['name']} - {dem['health']} health, {dem['damage'] :.2f} damage")
