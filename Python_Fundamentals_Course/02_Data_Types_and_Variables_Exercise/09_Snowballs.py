# •	On the first input line you will receive N – the number of snowballs.
# •	On the next N * 3 input lines you will be receiving data about snowballs.

number_of_snowballs = int(input())

highest_sv = 0
highest_ss = 0
highest_st = 0
highest_sq = 0

for snowball in range(number_of_snowballs):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_snow / snowball_time) ** snowball_quality
    if snowball_value > highest_sv:
        highest_sv = snowball_value
        highest_ss = snowball_snow
        highest_st = snowball_time
        highest_sq = snowball_quality

print(f"{highest_ss} : {highest_st} = {int(highest_sv)} ({highest_sq})")
