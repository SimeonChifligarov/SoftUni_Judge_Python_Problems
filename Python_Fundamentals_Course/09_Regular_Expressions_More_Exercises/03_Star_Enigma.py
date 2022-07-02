import re

number_of_messages = int(input())
attacked_planets = []
destroyed_planets = []

for _ in range(number_of_messages):
    current_message = input()
    key = current_message.count("s") + current_message.count("S") + current_message.count("t") + current_message.count(
        "T") + current_message.count("a") + current_message.count("A") + current_message.count(
        "r") + current_message.count("R")
    real_message = ""
    for index in range(len(current_message)):
        real_message += chr(ord(current_message[index]) - key)

    pattern = r"([^@!:>-]+)?@(?P<planet_name>[a-zA-Z]+)([^@!:>-]+)?:([^@!:>-]+)?(?P<planet_population>\d+)([^@!:>-]+)?!(?P<a_or_d>[AD])!([^@!:>-]+)?->(?P<soldiers_count>\d+)([^@!:>-]+)?"
    matches = re.match(pattern, real_message)
    if matches:
        matches_dict = matches.groupdict()
        if matches_dict['a_or_d'] == "A":
            attacked_planets.append(matches_dict['planet_name'])
        elif matches['a_or_d'] == "D":
            destroyed_planets.append(matches_dict['planet_name'])

print(f"Attacked planets: {len(attacked_planets)}")
for pl in sorted(attacked_planets):
    print(f"-> {pl}")
print(f"Destroyed planets: {len(destroyed_planets)}")
for pla in sorted(destroyed_planets):
    print(f"-> {pla}")
