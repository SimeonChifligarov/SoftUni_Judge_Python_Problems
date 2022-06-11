from collections import deque

START_COMMAND = "Start"
END_COMMAND = "End"
REFILL_COMMAND = "refill"

current_queue = deque([])

starting_water_quantity = int(input())
current_water_quantity = starting_water_quantity

while True:
    input_data = input()
    if input_data == START_COMMAND:
        break
    name = input_data
    current_queue.append(name)

while True:
    input_command = input()
    if input_command == END_COMMAND:
        break

    split_command = input_command.split()
    if split_command[0] == REFILL_COMMAND:
        refill_water_quantity = int(split_command[1])
        current_water_quantity += refill_water_quantity
    else:
        water_to_drink = int(split_command[0])
        current_person = current_queue.popleft()
        if water_to_drink <= current_water_quantity:
            current_water_quantity -= water_to_drink
            print(f"{current_person} got water")
        else:
            print(f"{current_person} must wait")

print(f"{current_water_quantity} liters left")
