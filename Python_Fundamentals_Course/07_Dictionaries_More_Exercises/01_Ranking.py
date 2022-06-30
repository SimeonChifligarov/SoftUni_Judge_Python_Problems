# "{contest}:{password for contest}" until you receive "end of contests

data = input()
contests_pass_dict = {}

while not data == "end of contests":
    split_data = data.split(":")
    contests_pass_dict[split_data[0]] = split_data[1]
    data = input()

submissions_dict = {}
total_points = {}
data_2 = input()

while not data_2 == "end of submissions":
    split_data_2 = data_2.split("=>")
    contest, password, username, points = split_data_2
    points = float(points)
    if contest in contests_pass_dict:
        if password == contests_pass_dict[contest]:
            if username not in submissions_dict:
                submissions_dict[username] = {}
                total_points[username] = 0
            if contest not in submissions_dict[username]:
                submissions_dict[username][contest] = points
                total_points[username] += points
            else:
                if submissions_dict[username][contest] < points:
                    total_points[username] += points - submissions_dict[username][contest]
                    submissions_dict[username][contest] = points

    data_2 = input()

for cand, score in total_points.items():
    if score == max(total_points.values()):
        print(f"Best candidate is {cand} with total {int(score)} points.")

sorted_submissions_dict = sorted(submissions_dict.items(), key=lambda x: x[0])

print("Ranking:")
for candidate, subms in sorted_submissions_dict:
    print(f"{candidate}")

    sorted_subms = sorted(subms.items(), key=lambda x: (-x[1]))
    for cont, pts in sorted_subms:
        print(f"#  {cont} -> {int(pts)}")
