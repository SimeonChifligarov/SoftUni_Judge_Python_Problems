from collections import deque

DATURA_BOMBS = 40
CHERRY_BOMBS = 60
SMOKE_DECOY_BOMBS = 120

bombs = {
    "Datura Bombs": 0,
    "Cherry Bombs": 0,
    "Smoke Decoy Bombs": 0,
}

bomb_effects = deque([int(el) for el in input().split(", ")])
bomb_castings = [int(el) for el in input().split(", ")]

# print(bomb_effects, bomb_castings)

while bomb_effects and bomb_castings:
    current_effect = bomb_effects.popleft()
    current_casting = bomb_castings.pop()

    if current_effect + current_casting == DATURA_BOMBS:
        bombs["Datura Bombs"] += 1
    elif current_effect + current_casting == CHERRY_BOMBS:
        bombs["Cherry Bombs"] += 1
    elif current_effect + current_casting == SMOKE_DECOY_BOMBS:
        bombs["Smoke Decoy Bombs"] += 1
    else:
        current_casting -= 5
        bomb_effects.appendleft(current_effect)
        bomb_castings.append(current_casting)

    if min(bombs.values()) >= 3:
        break

print("Bene! You have successfully filled the bomb pouch!" if min(
    bombs.values()) >= 3 else "You don't have enough materials to fill the bomb pouch.")

print(f"Bomb Effects: {', '.join([str(el) for el in bomb_effects]) if bomb_effects else 'empty'}")
print(f"Bomb Casings: {', '.join([str(el) for el in bomb_castings]) if bomb_castings else 'empty'}")
[print(f"{bomb}: {quantity}") for bomb, quantity in sorted(bombs.items())]

# # Solution 2
#
# from collections import deque
#
# bombs = {
#     "Datura Bombs": 0,
#     "Cherry Bombs": 0,
#     "Smoke Decoy Bombs": 0,
# }
#
# bomb_effects = deque([int(el) for el in input().split(", ")])
# bomb_castings = [int(el) for el in input().split(", ")]
#
# # print(bomb_effects, bomb_castings)
#
# while bomb_effects and bomb_castings:
#     current_effect = bomb_effects.popleft()
#     current_casting = bomb_castings.pop()
#
#     if current_effect + current_casting == 40:
#         bombs["Datura Bombs"] += 1
#     elif current_effect + current_casting == 60:
#         bombs["Cherry Bombs"] += 1
#     elif current_effect + current_casting == 120:
#         bombs["Smoke Decoy Bombs"] += 1
#     else:
#         current_casting -= 5
#         bomb_effects.appendleft(current_effect)
#         bomb_castings.append(current_casting)
#
#     if min(bombs.values()) >= 3:
#         break
#
# if min(bombs.values()) >= 3:
#     print("Bene! You have successfully filled the bomb pouch!")
# else:
#     print("You don't have enough materials to fill the bomb pouch.")
#
# if not bomb_effects:
#     print("Bomb Effects: empty")
# else:
#     print(f"Bomb Effects: {', '.join([str(el) for el in bomb_effects])}")
#
# if not bomb_castings:
#     print("Bomb Casings: empty")
# else:
#     print(f"Bomb Casings: {', '.join([str(el) for el in bomb_castings])}")
#
# for bomb, quantity in sorted(bombs.items()):
#     print(f"{bomb}: {quantity}")
