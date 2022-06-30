# "{player} -> {position} -> {skill}"
# "{player} vs {player}"

data = input()
players_pos_skill_dict = {}
player_totalskill = {}

while not data == "Season end":
    split_data = data.split(" -> ")
    if len(split_data) > 1:
        player = split_data[0]
        position = split_data[1]
        skill = int(split_data[2])
        if player not in players_pos_skill_dict:
            players_pos_skill_dict[player] = {}
            players_pos_skill_dict[player][position] = skill
            player_totalskill[player] = skill
        elif position not in players_pos_skill_dict[player]:
            players_pos_skill_dict[player][position] = skill
            player_totalskill[player] += skill
        else:
            if players_pos_skill_dict[player][position] < skill:
                player_totalskill[player] += skill - players_pos_skill_dict[player][position]
                players_pos_skill_dict[player][position] = skill
    elif len(split_data) == 1:
        new_split_data = data.split(" vs ")
        player = new_split_data[0]
        player_two = new_split_data[1]
        if not (player in player_totalskill and player_two in player_totalskill):
            data = input()
            continue
        for pos in players_pos_skill_dict[player]:
            if pos not in players_pos_skill_dict[player_two]:
                continue
            else:
                if player_totalskill[player] > player_totalskill[player_two]:
                    players_pos_skill_dict.pop(player_two)
                    player_totalskill.pop(player_two)
                    break
                elif player_totalskill[player] < player_totalskill[player_two]:
                    players_pos_skill_dict.pop(player)
                    player_totalskill.pop(player)
                    break
    data = input()

for plr, scr in sorted(player_totalskill.items(), key=lambda x: (-x[1], x[0])):
    print(f"{plr}: {scr} skill")
    for pos, pts in sorted(players_pos_skill_dict[plr].items(), key=lambda x: (-x[1], x[0])):
        print(f"- {pos} <::> {pts}")
