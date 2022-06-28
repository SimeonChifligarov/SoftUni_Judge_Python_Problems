# You will receive a to-do-notes until you get the command "End".
# The notes will be in the format: "{importance}-{value}".
# Return the list of to-do-notes sorted by importance. The maximum importance will be 10

to_do_chores = input()
all_chores = ["a"] * 11

while not to_do_chores == "End":
    importance, chore = to_do_chores.split("-")
    all_chores[int(importance)] = chore
    to_do_chores = input()

all_chores = [chore for chore in all_chores if not chore == "a"]
print(all_chores)
