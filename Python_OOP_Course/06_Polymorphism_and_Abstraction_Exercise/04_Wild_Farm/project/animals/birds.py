from project.animals.animal import Bird
from project.food import Food


class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food: Food):
        if type(food).__name__ not in ["Meat"]:
            return f"Owl does not eat {food.__class__.__name__}!"

        self.weight += 0.25 * food.quantity
        self.food_eaten += food.quantity


class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    def feed(self, food: Food):
        if type(food).__name__ not in ["Vegetable", "Fruit", "Meat", "Seed"]:
            return f"Hen does not eat {food.__class__.__name__}!"

        self.weight += 0.35 * food.quantity
        self.food_eaten += food.quantity


