# The input will consist of exactly 2 lines:
# •	party size – integer in range [1…100]
# •	days – integer in range [1…100]
import math

party_size = int(input())
days = int(input())

# You will receive a party size. After that you receive the days of the adventure.
# Every day, you are earning 50 coins, but you also spent 2 coins per companion for food.
# Every 3rd (third) day, you have a motivational party, spending 3 coins per companion for drinking water.
# Every 5th (fifth) day you slay a boss monster and you gain 20 coins per companion. But if you have a motivational
# party the same day, you spent additional 2 coins per companion.
# Every 10th (tenth) day at the start of the day, 2 (two) of your companions leave, but every 15th (fifteenth)
# day 5 (five) new companions are joined at the beginning of the day.

coins = 0

for day in range(1, days + 1):
    if day % 10 == 0:
        party_size -= 2
    if day % 15 == 0:
        party_size += 5
    coins += 50
    coins -= party_size * 2
    if day % 3 == 0:
        coins -= party_size * 3
    if day % 5 == 0:
        coins += party_size * 20
        if day % 3 == 0:
            coins -= party_size * 2

print(f"{party_size} companions received {math.floor(coins / party_size)} coins each.")
