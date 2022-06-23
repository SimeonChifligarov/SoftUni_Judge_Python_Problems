from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return "This pokemon is already caught"
        self.pokemons.append(pokemon)

        return f"Caught " + pokemon.pokemon_details()

    def release_pokemon(self, pokemon_name: str):
        pokemon_of_interest = [p for p in self.pokemons if p.name == pokemon_name]
        if not pokemon_of_interest:
            return "Pokemon is not caught"

        pokemon_of_interest = pokemon_of_interest[0]
        self.pokemons.remove(pokemon_of_interest)
        return f"You have released {pokemon_name}"

    def trainer_data(self):
        trainer_data_result = [
            f"Pokemon Trainer {self.name}",
            f"Pokemon count {len(self.pokemons)}",
            ]

        for current_pokemon in self.pokemons:
            trainer_data_result.append(f"- " + current_pokemon.pokemon_details())
        return "\n".join(trainer_data_result)

#
# pokemon = Pokemon("Pikachu", 90)
# print(pokemon.pokemon_details())
# trainer = Trainer("Ash")
# print(trainer.add_pokemon(pokemon))
# second_pokemon = Pokemon("Charizard", 110)
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.trainer_data())
#