data = input()
contests_dict = {}
ind_dict = {}

while not data == "no more time":
    split_data = data.split(" -> ")
    username, contest, points = split_data
    points = int(points)
    if username not in ind_dict:
        ind_dict[username] = 0
    if contest not in contests_dict:
        contests_dict[contest] = {}
    if username not in contests_dict[contest]:
        contests_dict[contest][username] = points
        ind_dict[username] += points
    else:
        if contests_dict[contest][username] < points:
            ind_dict[username] += points - contests_dict[contest][username]
            contests_dict[contest][username] = points

    data = input()

for contest, participants in contests_dict.items():
    print(f"{contest}: {len(participants)} participants")
    sorted_participants = sorted(participants.items(), key=lambda x: (-x[1], x[0]))
    place = 0
    for participant, score in sorted_participants:
        place += 1
        print(f"{place}. {participant} <::> {score}")

print("Individual standings:")
sorted_ind = sorted(ind_dict.items(), key=lambda x: (-x[1], x[0]))
place = 0
for name, pts in sorted_ind:
    place += 1
    print(f"{place}. {name} -> {pts}")
