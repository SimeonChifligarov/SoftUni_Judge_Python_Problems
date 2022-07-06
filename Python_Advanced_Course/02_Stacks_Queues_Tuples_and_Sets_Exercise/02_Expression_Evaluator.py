import functools

expression_as_list = input().split()

current_list = []
result = 0

math_operators = {'*', '+', '-', '/'}

for el in expression_as_list:
    if el in math_operators:
        if el == '*':
            result = functools.reduce(lambda a, b: a * b, current_list)
        elif el == '+':
            result = functools.reduce(lambda a, b: a + b, current_list)
        elif el == '-':
            result = functools.reduce(lambda a, b: a - b, current_list)
        elif el == '/':
            result = functools.reduce(lambda a, b: a // b, current_list)
        current_list = [result]
    else:
        current_list.append(int(el))

print(result)
