# You will be receiving key-value pairs on separate lines separated by ": " until you receive the command "statistics".

data = input()
products_dict = {}

while not data == "statistics":
    product, quantity = data.split(": ")
    quantity = int(quantity)
    if product not in products_dict:
        products_dict[product] = 0
    products_dict[product] += quantity
    data = input()

print("Products in stock:")
for prod, quant in products_dict.items():
    print(f"- {prod}: {quant}")
print(f"Total Products: {len(products_dict)}")
print(f"Total Quantity: {sum(products_dict.values())}")
