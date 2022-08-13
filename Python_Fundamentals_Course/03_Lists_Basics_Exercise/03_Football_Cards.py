# stupid problem

string_of_cards = input().split()
team_a_cards = []
team_b_cards = []

for card in string_of_cards:
    if "A-" in card:
        team_a_cards.append(card)
    elif "B-" in card:
        team_b_cards.append(card)

red_a = len(set(team_a_cards))
red_b = len(set(team_b_cards))
if red_a > 5:
    red_a = 5
if red_b > 5:
    red_b = 5
print(f'Team A - {11 - red_a}; Team B - {11 - red_b}')
if red_a == 5 or red_b == 5:
    print('Game was terminated')
