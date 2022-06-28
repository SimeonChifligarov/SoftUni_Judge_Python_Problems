# 4.	Social Distribution from More Exercises: Lists Advanced

population_list = [int(el) for el in input().split(", ")]

minimum_wealth = int(input())

for index in range(len(population_list)):
    if population_list[index] < minimum_wealth:
        population_list[population_list.index(max(population_list))] -= minimum_wealth - population_list[index]
        population_list[index] = minimum_wealth

if min(population_list) < minimum_wealth:
    print('No equal distribution possible')
else:
    print(population_list)
