#

number_of_plants = int(input())

all_plants = {}

for _ in range(number_of_plants):
    plant, rarity = input().split("<->")
    all_plants[plant] = {'rarity': int(rarity), 'ratings': []}

command = input()

while not command == "Exhibition":
    split_command = command.split(": ")
    real_command = split_command[0]
    if real_command == "Rate":
        plant, rating = split_command[1].split(" - ")
        if plant in all_plants:
            all_plants[plant]['ratings'].append(int(rating))
        else:
            print("error")
    elif real_command == "Update":
        plant, new_rarity = split_command[1].split(" - ")
        if plant in all_plants:
            all_plants[plant]['rarity'] = int(new_rarity)
        else:
            print("error")
    elif real_command == "Reset":
        plant = split_command[1]
        if plant in all_plants:
            all_plants[plant]['ratings'].clear()
        else:
            print("error")
    else:
        print("error")

    command = input()

for pla, stats in all_plants.items():
    if stats['ratings']:
        avg_rating = sum(stats['ratings']) / len(stats['ratings'])
        all_plants[pla]['avg_rating'] = avg_rating
    else:
        all_plants[pla]['avg_rating'] = 0

# sorted_plants = sorted(all_plants.items(), key=lambda x: (-x[1]['rarity'], -x[1]['avg_rating']))

print("Plants for the exhibition:")
# for curr_plant, stats in sorted_plants:
for curr_plant, stats in all_plants.items():
    print(f"- {curr_plant}; Rarity: {stats['rarity']}; Rating: {stats['avg_rating'] :.2f}")
