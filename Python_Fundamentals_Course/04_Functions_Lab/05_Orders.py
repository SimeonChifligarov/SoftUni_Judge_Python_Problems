# Write a function that calculates the total price of an order and prints it on the console.
# The function should receive one of the following products: coffee, coke, water, snacks; and a quantity of the product.
# The prices for a single piece of each product are:
# •	coffee - 1.50
# •	water - 1.00
# •	coke - 1.40
# •	snacks - 2.00
# Print the result formatted to the second decimal place.

def total_price_of_order(order_type, order_quantity):
    total_price = None
    if order_type == "coffee":
        total_price = order_quantity * 1.50
    elif order_type == "coke":
        total_price = order_quantity * 1.40
    elif order_type == "water":
        total_price = order_quantity * 1.00
    elif order_type == "snacks":
        total_price = order_quantity * 2.00
    return total_price


product = input()
quantity = int(input())
print(f'{total_price_of_order(product, quantity):.2f}')
