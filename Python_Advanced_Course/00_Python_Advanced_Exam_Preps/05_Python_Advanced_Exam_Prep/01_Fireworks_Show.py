from collections import deque

fireworks_as_dict = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0,
}

firework_effects = deque([int(el) for el in input().split(", ")])
explosive_power = deque([int(el) for el in input().split(", ")])

while firework_effects and explosive_power:
    current_firework_effect = firework_effects[0]
    current_explosive_power = explosive_power[-1]

    if current_firework_effect <= 0:
        firework_effects.popleft()
        continue
    if current_explosive_power <= 0:
        explosive_power.pop()
        continue

    current_sum_effect_plus_power = current_firework_effect + current_explosive_power

    if current_sum_effect_plus_power % 15 == 0:
        fireworks_as_dict["Crossette Fireworks"] += 1
        firework_effects.popleft()
        explosive_power.pop()
    elif current_sum_effect_plus_power % 5 == 0:
        fireworks_as_dict["Willow Fireworks"] += 1
        firework_effects.popleft()
        explosive_power.pop()
    elif current_sum_effect_plus_power % 3 == 0:
        fireworks_as_dict["Palm Fireworks"] += 1
        firework_effects.popleft()
        explosive_power.pop()

    else:
        firework_effects[0] -= 1
        firework_effects.append(firework_effects.popleft())

    if min(fireworks_as_dict.values()) >= 3:
        break

if min(fireworks_as_dict.values()) >= 3:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if firework_effects:
    print(f"Firework Effects left: {', '.join([str(el) for el in firework_effects])}")
if explosive_power:
    print(f"Explosive Power left: {', '.join([str(el) for el in explosive_power])}")

for firework_type, count in fireworks_as_dict.items():
    print(f"{firework_type}: {count}")
