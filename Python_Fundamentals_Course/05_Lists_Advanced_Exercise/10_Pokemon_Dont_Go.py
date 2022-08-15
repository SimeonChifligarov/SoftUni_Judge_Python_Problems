pokemons = [int(el) for el in input().split()]

total_sum = 0

while pokemons:
    index = int(input())

    if 0 <= index < len(pokemons):
        element = pokemons[index]

        pokemons = pokemons[:index] + pokemons[index + 1:]
        total_sum += element

        for i in range(len(pokemons)):
            if pokemons[i] <= element:
                pokemons[i] += element
            else:
                pokemons[i] -= element
    elif index < 0:
        element = pokemons[0]
        total_sum += element

        pokemons = [pokemons[-1]] + pokemons[1:]
        for i in range(len(pokemons)):
            if pokemons[i] <= element:
                pokemons[i] += element
            else:
                pokemons[i] -= element
    elif index > len(pokemons) - 1:
        element = pokemons[-1]
        total_sum += element

        pokemons = pokemons[:-1] + [pokemons[0]]
        for i in range(len(pokemons)):
            if pokemons[i] <= element:
                pokemons[i] += element
            else:
                pokemons[i] -= element
    # print(pokemons)
    # print(total_sum)
    # print('======')

print(total_sum)
