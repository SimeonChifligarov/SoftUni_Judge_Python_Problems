class Shop:
    SMALL_SHOP_CAPACITY = 10
    NOT_ENOUGH_CAPACITY_MESSAGE = "Not enough capacity in the shop"

    def __init__(self, name, type_store, capacity):
        self.name = name
        self.type = type_store
        self.capacity = capacity
        self.items = {}

    @classmethod
    def small_shop(cls, name, type_store):
        return cls(name, type_store, Shop.SMALL_SHOP_CAPACITY)

    def add_item(self, item_name):
        if self.__current_items_quantity() >= self.capacity:
            return self.NOT_ENOUGH_CAPACITY_MESSAGE

        if item_name not in self.items:
            self.items[item_name] = 0
        self.items[item_name] += 1
        return self.__get_successful_add_item_message(item_name)

    def remove_item(self, item_name, count):
        if item_name not in self.items or self.items[item_name] < count:
            return self.__get_unsuccessful_remove_item_message(item_name, count)

        self.items[item_name] -= count
        if self.items[item_name] == 0:
            del self.items[item_name]
        return self.__get_successful_remove_item_message(item_name, count)

    def __current_items_quantity(self):
        return sum([v for v in self.items.values()])

    @staticmethod
    def __get_successful_add_item_message(item_name):
        return f'{item_name} added to the shop'

    @staticmethod
    def __get_unsuccessful_remove_item_message(item_name, amount):
        return f'Cannot remove {amount} {item_name}'

    @staticmethod
    def __get_successful_remove_item_message(item_name, amount):
        return f'{amount} {item_name} removed from the shop'

    def __repr__(self):
        return f'{self.name} of type {self.type} with capacity {self.capacity}'

# fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
# small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
# print(fresh_shop)
# print(small_shop)
#
# print(fresh_shop.add_item("Bananas"))
# print(fresh_shop.remove_item("Tomatoes", 2))
#
# print(small_shop.add_item("Jeans"))
# print(small_shop.add_item("Jeans"))
# print(small_shop.remove_item("Jeans", 2))
# print(small_shop.items)
