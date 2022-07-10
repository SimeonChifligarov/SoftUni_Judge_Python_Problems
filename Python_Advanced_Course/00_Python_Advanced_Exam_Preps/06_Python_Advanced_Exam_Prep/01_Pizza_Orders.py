from collections import deque

pizza_orders = deque([int(el) for el in input().split(", ")])
employees_capacity = [int(el) for el in input().split(", ")]

# print(pizza_orders)

total_pizzas = 0
rest_of_pizza = []

while pizza_orders and employees_capacity:
    current_pizza = pizza_orders[0]
    current_employee = employees_capacity[-1]

    if current_pizza > 10 or current_pizza <= 0:
        pizza_orders.popleft()
        continue

    if current_pizza <= current_employee:
        total_pizzas += current_pizza
        if rest_of_pizza:
            total_pizzas += sum(rest_of_pizza)
            rest_of_pizza = []
        pizza_orders.popleft()
        employees_capacity.pop()

    else:
        pizza_orders[0] -= current_employee
        rest_of_pizza.append(current_employee)
        employees_capacity.pop()

if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas}")
    print(f"Employees: {', '.join([str(el) for el in employees_capacity])}")

else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(el) for el in pizza_orders])}")
