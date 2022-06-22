class PizzaDelivery:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, price_per_ingredient: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        if ingredient not in self.ingredients:
            self.ingredients[ingredient] = 0
        self.ingredients[ingredient] += quantity
        self.price += quantity * price_per_ingredient

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_ingredient: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"

        if self.ingredients[ingredient] < quantity:
            return f"Please check again the desired quantity of {ingredient}!"

        self.ingredients[ingredient] -= quantity
        self.price -= quantity * price_per_ingredient

    def make_order(self):
        self.ordered = True
        ingredients_result = ", ".join([f"{ingr}: {quant}" for ingr, quant in self.ingredients.items()])
        return f"You've ordered pizza {self.name} prepared " \
               f"with {ingredients_result} and the price will be {self.price}lv."
