set_of_odds = set()
set_of_evens = set()

names_count = int(input())

for i in range(names_count):
    name = input()
    line = i + 1

    ascii_sum = 0
    for letter in name:
        ascii_sum += ord(letter)

    name_sum = ascii_sum // line

    if name_sum % 2 == 0:
        set_of_evens.add(name_sum)
    else:
        set_of_odds.add(name_sum)

if sum(set_of_odds) == sum(set_of_evens):
    union_values = set_of_odds.union(set_of_evens)
    result = union_values
elif sum(set_of_odds) > sum(set_of_evens):
    different_values = set_of_odds.difference(set_of_evens)
    result = different_values
else:
    symmetric_difference_values = set_of_odds.symmetric_difference(set_of_evens)
    result = symmetric_difference_values

print(*result, sep=", ")
