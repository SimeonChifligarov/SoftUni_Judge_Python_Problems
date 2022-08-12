# The input will consist of 5 lines:
# •	On the first line you will receive the lost fights count – integer in the range [0, 1000].
# •	On the second line you will receive the helmet price - floating point number in range [0, 1000].
# •	On the third line you will receive the sword price - floating point number in range [0, 1000].
# •	On the fourth line you will receive the shield price - floating point number in range [0, 1000].
# •	On the fifth line you will receive the armor price - floating point number in range [0, 1000].

fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

# Every second lost game, his helmet is broken.
# Every third lost game, his sword is broken.
# When both his sword and helmet are broken in the same lost fight, his shield also brakes.
# Every second time, when his shield brakes, his armor also needs to be repaired.

expenses = 0
shield_brakes_count = 0

for lost_game in range(1, fights_count + 1):
    if lost_game % 2 == 0:
        expenses += helmet_price
    if lost_game % 3 == 0:
        expenses += sword_price
        if lost_game % 2 == 0:
            expenses += shield_price
            shield_brakes_count += 1
            if shield_brakes_count % 2 == 0:
                expenses += armor_price

print(f"Gladiator expenses: {expenses :.2f} aureus")
