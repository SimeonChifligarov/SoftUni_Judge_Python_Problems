alphabet_order = {chr(num + 96): num for num in range(1, 27)}

data = input().split()

number = 0
total_sum = 0
for el in data:
    current_result = 0
    number = int(el[1:-1])
    if el[0].isupper():
        position = alphabet_order[el[0].lower()]
        current_result = number / position
    elif el[0].islower():
        position = alphabet_order[el[0]]
        current_result = number * position
    if el[-1].isupper():
        position = alphabet_order[el[-1].lower()]
        current_result -= position
    elif el[-1].islower():
        position = alphabet_order[el[-1]]
        current_result += position
    total_sum += current_result
print(f"{total_sum:.2f}")

# # Solution 2
# alphabet_order = {chr(num + 96): num for num in range(1, 27)}
#
# data = input().split()
#
# number = 0
# current_result = 0
# total_sum = 0
# for el in data:
#     number = int(el[1:-1])
#     if el[0].isupper():
#         position = alphabet_order[el[0].lower()]
#         current_result = number / position
#     elif el[0].islower():
#         position = alphabet_order[el[0]]
#         current_result = number * position
#     if el[-1].isupper():
#         position = alphabet_order[el[-1].lower()]
#         current_result -= position
#     elif el[-1].islower():
#         position = alphabet_order[el[-1]]
#         current_result += position
#     total_sum += current_result
# print(f"{total_sum:.2f}")
