import re

pattern = r">>(?P<furniture>\w+)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)"

data_as_line = input()
all_furniture = []
total_price = 0

while not data_as_line == "Purchase":
    current_furniture = re.fullmatch(pattern, data_as_line)
    if current_furniture:
        all_furniture.append(current_furniture['furniture'])
        total_price += float(current_furniture['price']) * int(current_furniture['quantity'])
    data_as_line = input()

print("Bought furniture:")
for furn in all_furniture:
    print(furn)
print(f"Total money spend: {total_price :.2f}")

# # Solution 2
# import re
#
# pattern = r">>(?P<furniture>\w+)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)"
#
# data_as_line = input()
# all_furnitures = []
# total_price = 0
#
# while not data_as_line == "Purchase":
#     current_furniture = [el.groupdict() for el in re.finditer(pattern, data_as_line)]
#     if current_furniture:
#         all_furnitures.append(current_furniture[0]['furniture'])
#         total_price += float(current_furniture[0]['price']) * int(current_furniture[0]['quantity'])
#     data_as_line = input()
#
# print("Bought furniture:")
# for furn in all_furnitures:
#     print(furn)
# print(f"Total money spend: {total_price :.2f}")
