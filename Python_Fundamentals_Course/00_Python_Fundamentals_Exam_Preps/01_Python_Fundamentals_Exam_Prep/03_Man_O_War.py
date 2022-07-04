# •	On the 1st line you are going to receive the status of the pirate ship (integers separated by '>')
# •	On the 2nd line you are going to receive the status of the warship
# •	On the 3rd line you are going receive the maximum health a section of a ship can reach.
# •	On the next lines, until "Retire", you will be receiving commands.

status_pirate_ship = [int(el) for el in input().split(">")]
status_of_the_warship = [int(el) for el in input().split(">")]
max_health = int(input())
stalemate = True
full_command = input()

while not full_command == "Retire":
    full_command = full_command.split()
    real_command = full_command[0]
    if real_command == "Fire":
        index = int(full_command[1])
        damage = int(full_command[2])
        if index in range(len(status_of_the_warship)):
            status_of_the_warship[index] -= damage
            if status_of_the_warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                stalemate = False
                break
    elif real_command == "Defend":
        start_index = int(full_command[1])
        end_index = int(full_command[2])
        damage = int(full_command[3])
        if start_index in range(len(status_pirate_ship)) and end_index in range(len(status_pirate_ship)):
            for current_index in range(start_index, end_index + 1):
                status_pirate_ship[current_index] -= damage
                if status_pirate_ship[current_index] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    stalemate = False
                    break
    elif real_command == "Repair":
        index = int(full_command[1])
        health = int(full_command[2])
        if index in range(len(status_pirate_ship)):
            if status_pirate_ship[index] + health < max_health:
                status_pirate_ship[index] += health
            else:
                status_pirate_ship[index] = max_health
    elif real_command == "Status":
        needed_repair = [el for el in status_pirate_ship if el < max_health * 0.20]
        print(f"{len(needed_repair)} sections need repair.")
        needed_repair = []
    full_command = input()
if stalemate:
    print(f"Pirate ship status: {sum(status_pirate_ship)}")
    print(f"Warship status: {sum(status_of_the_warship)}")
