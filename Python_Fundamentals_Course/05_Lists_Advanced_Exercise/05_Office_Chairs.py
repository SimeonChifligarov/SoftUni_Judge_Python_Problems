# You will be given a number n representing how many rooms there are.
# On the next n lines for each room you will get how many chairs there are
# and how many of them will be taken. The chairs will be represented by "X"s,
# then there will be a space " " and a number representing the taken places.
# Example: "XXXXX 4"

number_of_rooms = int(input())

free_chairs = 0
fails = 0
for room in range(1, number_of_rooms + 1):
    chairs, people = input().split()
    people = int(people)

    # if you get to a room where there are more people than chairs,
    # print the following message: "{needed_chairs_in_room} more chairs needed
    # in room {number_of_room}". If there is enough chairs
    # in each room print: "Game On, {total_free_chairs} free chairs left"

    if people > len(chairs):
        print(f"{people - len(chairs)} more chairs needed in room {room}")
        fails += 1
    else:
        free_chairs += len(chairs) - people

if fails == 0:
    print(f'Game On, {free_chairs} free chairs left')
