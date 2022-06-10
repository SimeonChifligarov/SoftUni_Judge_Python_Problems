# # solution_1
# # does not follow the requirements
#
# print(input()[::-1])

# # solution_2
# # input as a string is a collection (of chars)
#
# text = input()
# stack = []
#
# for i in range(len(text)):
#     stack.append(text[-i - 1])
#
# print("".join(stack))

# solution_3
# using both stack and list

text_as_list = list(input())
stack = []

for i in range(len(text_as_list)):
    stack.append(text_as_list.pop())

print("".join(stack))
