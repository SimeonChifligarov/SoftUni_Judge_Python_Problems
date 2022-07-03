from collections import deque

food_quantity = int(input())
food_left = food_quantity

quantity_of_order = deque([int(el) for el in input().split()])

print(max(quantity_of_order))

while quantity_of_order:
    current_order = quantity_of_order.popleft()

    if current_order <= food_left:
        food_left -= current_order
    else:
        quantity_of_order.appendleft(current_order)
        break

if quantity_of_order:
    print(f"Orders left: {' '.join([str(el) for el in quantity_of_order])}")
else:
    print("Orders complete")
