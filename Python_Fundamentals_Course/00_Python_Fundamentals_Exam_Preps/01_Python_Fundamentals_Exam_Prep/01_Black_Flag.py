# •	On the 1st line you will receive the days of the plunder – an integer number in the range [0…100000]
# •	On the 2nd line you will receive the daily plunder – an integer number in the range [0…50]
# •	On the 3rd line you will receive the expected plunder – a real number in the range [0.0…10000.0]

days_of_plunder = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
total_plunder = 0

for day in range(1, days_of_plunder + 1):
    total_plunder += daily_plunder
    if day % 3 == 0:
        total_plunder += 0.5 * daily_plunder
    if day % 5 == 0:
        total_plunder *= 0.7

if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder :.2f} plunder gained.")
else:
    print(f"Collected only {total_plunder / expected_plunder * 100 :.2f}% of the plunder.")
