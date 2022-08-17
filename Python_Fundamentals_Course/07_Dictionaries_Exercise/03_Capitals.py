# # Solution 1
# countries = input().split(', ')
# capitals = input().split(', ')
#
# result = {}
#
# for i in range(len(countries)):
#     result[countries[i]] = capitals[i]
#
# for country, capital in result.items():
#     print(f'{country} -> {capital}')

# # Solution 2
# countries = input().split(', ')
# capitals = input().split(', ')
#
# result = {countries[i]: capitals[i] for i in range(len(countries))}
#
# for country, capital in result.items():
#     print(f'{country} -> {capital}')

# Solution 3
countries = input().split(', ')
capitals = input().split(', ')

countries_dict = zip(countries, capitals)
# print(list(countries_dict))

result = {el[0]: el[1] for el in countries_dict}

for country, capital in result.items():
    print(f'{country} -> {capital}')
