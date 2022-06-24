# Beaches are filled with sand, water, fish, and sun. Given a string, calculate how many times the words "Sand", "Water", "Fish", and "Sun" appear (case insensitive).

string = input()

string_allcaps = string.upper()

score = string_allcaps.count("SAND") + string_allcaps.count("WATER") + string_allcaps.count(
    "FISH") + string_allcaps.count("SUN")

print(score)
