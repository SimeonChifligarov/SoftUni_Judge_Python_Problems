# The input will be on two lines:
# •	On the first line, you will receive n – the number of lines, which will follow
# •	On the next n lines – you receive quantities of water, which you have to pour in the tank

number_of_lines = int(input())
CAPACITY = 255
current_water = 0

for pour in range(number_of_lines):
    water = int(input())
    current_water += water
    if current_water > CAPACITY:
        print("Insufficient capacity!")
        current_water -= water

print(current_water)

# # Solution 2
# CAPACITY = 255
# water_in_tank = 0
# poured_times = int(input())
#
# for pour in range(1, poured_times+1):
#     poured_water = int(input())
#     water_in_tank += poured_water
#     if water_in_tank > CAPACITY:
#         print('Insufficient capacity!')
#         water_in_tank -= poured_water
# print(water_in_tank)
