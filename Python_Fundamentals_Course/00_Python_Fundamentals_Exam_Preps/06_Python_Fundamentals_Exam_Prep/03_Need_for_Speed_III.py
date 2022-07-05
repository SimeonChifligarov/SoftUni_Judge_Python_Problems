#

number_of_cars = int(input())
all_cars = {}

for _ in range(number_of_cars):
    car_data = input().split("|")
    car = car_data[0]
    mileage = int(car_data[1])
    fuel = int(car_data[2])
    if car not in all_cars:
        all_cars[car] = {"mileage": 0, "fuel": 0}
    all_cars[car]["mileage"] += mileage
    all_cars[car]["fuel"] += fuel

command = input()

while not command == "Stop":
    split_command = command.split(" : ")
    real_command = split_command[0]
    if real_command == "Drive":
        curr_car = split_command[1]
        distance = int(split_command[2])
        fuel_needed = int(split_command[3])
        if fuel_needed > all_cars[curr_car]["fuel"]:
            print("Not enough fuel to make that ride")
        else:
            all_cars[curr_car]["mileage"] += distance
            all_cars[curr_car]["fuel"] -= fuel_needed
            print(f"{curr_car} driven for {distance} kilometers. {fuel_needed} liters of fuel consumed.")
        if all_cars[curr_car]["mileage"] >= 100000:
            print(f"Time to sell the {curr_car}!")
            all_cars.pop(curr_car)
    elif real_command == "Refuel":
        curr_car = split_command[1]
        refueled = int(split_command[2])
        current_fuel = all_cars[curr_car]["fuel"]
        if current_fuel + refueled <= 75:
            all_cars[curr_car]["fuel"] += refueled
            print(f"{curr_car} refueled with {refueled} liters")
        else:
            all_cars[curr_car]["fuel"] = 75
            print(f"{curr_car} refueled with {75 - current_fuel} liters")
    elif real_command == "Revert":
        curr_car = split_command[1]
        kilometers = int(split_command[2])
        all_cars[curr_car]["mileage"] -= kilometers
        if all_cars[curr_car]["mileage"] < 10000:
            all_cars[curr_car]["mileage"] = 10000
        else:
            print(f"{curr_car} mileage decreased by {kilometers} kilometers")

    command = input()

# sorted_all_cars = sorted(all_cars.items(), key=lambda x: (-x[1]["mileage"], x[0]))

# for this_car, stats in sorted_all_cars:
for this_car, stats in all_cars.items():
    print(f"{this_car} -> Mileage: {stats['mileage']} kms, Fuel in the tank: {stats['fuel']} lt.")
