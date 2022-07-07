input_as_lists = input().split('|')
# print(input_as_lists)

result = []
for el in input_as_lists[::-1]:
    current_list = [int(el) for el in el.split()]
    result.append(current_list)

[print(el, end=' ') for submatrix in result for el in submatrix]
