from project.animals.animal import Mammal
from project.food import Food


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    def feed(self, food: Food):
        if type(food).__name__ not in ["Vegetable", "Fruit"]:
            return f"Mouse does not eat {food.__class__.__name__}!"

        self.weight += 0.10 * food.quantity
        self.food_eaten += food.quantity


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    def feed(self, food: Food):
        if type(food).__name__ not in ["Meat"]:
            return f"Dog does not eat {food.__class__.__name__}!"

        self.weight += 0.40 * food.quantity
        self.food_eaten += food.quantity


class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"

    def feed(self, food: Food):
        if type(food).__name__ not in ["Vegetable", "Meat"]:
            return f"Cat does not eat {food.__class__.__name__}!"

        self.weight += 0.30 * food.quantity
        self.food_eaten += food.quantity


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food: Food):
        if type(food).__name__ not in ["Meat"]:
            return f"Tiger does not eat {food.__class__.__name__}!"

        self.weight += 1.00 * food.quantity
        self.food_eaten += food.quantity
