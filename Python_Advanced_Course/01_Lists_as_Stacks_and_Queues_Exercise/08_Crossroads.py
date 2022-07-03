from collections import deque

green_light_duration = int(input())
free_window = int(input())

remaining_cars = deque([])
cars_passed = 0

crash = False
while True:
    command = input()
    if command == "END":
        break

    if command == "green":
        time_left = green_light_duration

        while time_left > 0 and remaining_cars:
            current_car = remaining_cars.popleft()
            if len(current_car) <= time_left:
                time_left -= len(current_car)
                cars_passed += 1

            elif len(current_car) <= time_left + free_window:
                cars_passed += 1
                break

            else:
                crash = True
                print("A crash happened!")
                print(f"{current_car} was hit at {current_car[time_left + free_window:][0]}.")
                break

    if crash:
        break

    else:
        car = command
        remaining_cars.append(car)

if not crash:
    print("Everyone is safe.")
    print(f"{cars_passed} total cars passed the crossroads.")
