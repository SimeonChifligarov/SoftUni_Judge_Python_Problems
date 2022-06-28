# You will receive how many wagons the train has. Create a list with that length with all zeros.
# Until you receive the command "End", you get some of the following commands:
# •	add {people} -> adds the people in the last wagon
# •	insert {index} {people} -> adds the people at the given wagon
# •	leave {index} {people} -> removes the people from the wagon
# After you receive the "End" command print the train

number_of_wagons = int(input())
wagons_people = [0] * number_of_wagons

command_full = input()

while not command_full == "End":
    command_full = command_full.split()
    command = command_full[0]
    if command == "add":
        wagons_people[-1] += int(command_full[-1])
    elif command == "insert":
        insert_index = int(command_full[1])
        insert_people = int(command_full[2])
        wagons_people[insert_index] += insert_people
    elif command == "leave":
        leave_index = int(command_full[1])
        leave_people = int(command_full[2])
        wagons_people[leave_index] -= leave_people
    command_full = input()

print(wagons_people)
