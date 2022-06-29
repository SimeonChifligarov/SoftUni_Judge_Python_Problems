# Create a class Zoo. It should have a class attribute called __animals that stores
# the total count of the animals in the zoo. The __init__ method should only receive the name of the zoo.
# There you should also create 3 empty lists (mammals, fishes, birds). The class should also have 2 more methods:
# •	add_animal(species, name) - based on the species adds the name to the corresponding list
# •	get_info(species) - based on the species returns a string in the following format:
# "{Species} in {zoo_name}: {names}" and on another line "Total animals: {total_animals}"

class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        Zoo.__animals += 1
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

    def get_info(self, species):
        if species == "mammal":
            return f"{species.capitalize()}s in {self.zoo_name}: {', '.join(self.mammals)}\nTotal animals: {Zoo.__animals}"
        elif species == "fish":
            return f"{species.capitalize()}es in {self.zoo_name}: {', '.join(self.fishes)}\nTotal animals: {Zoo.__animals}"
        elif species == "bird":
            return f"{species.capitalize()}s in {self.zoo_name}: {', '.join(self.birds)}\nTotal animals: {Zoo.__animals}"


name_of_the_zoo = input()
my_zoo = Zoo(name_of_the_zoo)
number_of_animals = int(input())
for animal in range(number_of_animals):
    species_name = input().split()
    my_zoo.add_animal(species_name[0], species_name[1])

species_info = input()

print(my_zoo.get_info(species_info))
