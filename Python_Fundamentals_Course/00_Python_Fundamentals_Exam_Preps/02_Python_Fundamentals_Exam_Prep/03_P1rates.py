#

command = input()
cities = {}

while not command == "Sail":
    command_split = command.split("||")
    city_name = command_split[0]
    city_population = int(command_split[1])
    city_gold = int(command_split[2])
    if city_name not in cities:
        cities[city_name] = {'population': 0, 'gold': 0}
    cities[city_name]['population'] += city_population
    cities[city_name]['gold'] += city_gold
    command = input()

while not command == "End":
    split_command = command.split("=>")
    real_command = split_command[0]
    if real_command == "Plunder":
        city_n = split_command[1]
        city_p = int(split_command[2])
        city_g = int(split_command[3])
        if city_n in cities:
            cities[city_n]['population'] -= city_p
            cities[city_n]['gold'] -= city_g
            print(f"{city_n} plundered! {city_g} gold stolen, {city_p} citizens killed.")
            if cities[city_n]['population'] <= 0 or cities[city_n]['gold'] <= 0:
                print(f"{city_n} has been wiped off the map!")
                cities.pop(city_n)
    elif real_command == "Prosper":
        city_na = split_command[1]
        city_go = int(split_command[2])
        if city_go < 0:
            print(f"Gold added cannot be a negative number!")
        elif city_na in cities:
            cities[city_na]['gold'] += city_go
            print(f"{city_go} gold added to the city treasury. {city_na} now has {cities[city_na]['gold']} gold.")
    command = input()

if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    # sorted_cities = sorted(cities.items(), key=lambda x: (-x[1]['gold'], x[0]))

    # for cit in sorted_cities:
    for cit in cities.items():
        print(f"{cit[0]} -> Population: {cit[1]['population']} citizens, Gold: {cit[1]['gold']} kg")

else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
