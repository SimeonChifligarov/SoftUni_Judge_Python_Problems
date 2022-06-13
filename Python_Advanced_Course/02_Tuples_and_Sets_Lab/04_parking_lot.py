number_of_commands = int(input())

cars_in_parking = set()

for _ in range(number_of_commands):
    direction, car_number = input().split(", ")
    if direction == "IN":
        cars_in_parking.add(car_number)
    elif direction == "OUT":
        cars_in_parking.remove(car_number)

if cars_in_parking:
    print(*cars_in_parking, sep="\n")
else:
    print("Parking Lot is Empty")
