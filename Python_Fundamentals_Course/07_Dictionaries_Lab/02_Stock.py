# You will receive a single line containing some food (keys) and quantities (values).
# They will be separated by a single space (the first element is the key, the second – the value and so on).

# On the next line you will be given products to search for. Check for each product, you have 2 possibilities:

food_and_quantity = input().split()
products_to_search = input().split()
dict_foods = {}

for index in range(0, len(food_and_quantity) - 1, 2):
    food = food_and_quantity[index]
    quantity = int(food_and_quantity[index + 1])
    dict_foods[food] = quantity

for product in products_to_search:
    if product not in dict_foods:
        print(f"Sorry, we don't have {product}")
    else:
        print(f"We have {dict_foods[product]} of {product} left")
