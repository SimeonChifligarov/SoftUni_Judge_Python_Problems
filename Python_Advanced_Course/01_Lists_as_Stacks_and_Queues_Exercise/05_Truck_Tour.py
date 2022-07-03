from collections import deque

petrol_pumps = int(input())

pumps_stats = deque([])

for _ in range(petrol_pumps):
    petrol, distance = [int(el) for el in input().split()]
    current_pump_value = petrol - distance
    pumps_stats.append(current_pump_value)

for i in range(petrol_pumps):
    all_fuel_status = [pumps_stats[0]]
    for j in range(1, petrol_pumps):
        all_fuel_status.append(all_fuel_status[-1] + pumps_stats[j])
    if all(n >= 0 for n in all_fuel_status):
        print(i)
        break
    pumps_stats.rotate(-1)
