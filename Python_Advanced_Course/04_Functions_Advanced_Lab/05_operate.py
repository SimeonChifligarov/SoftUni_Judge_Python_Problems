def operate(operator, *args):
    result = args[0]
    rest_of_args = args[1:]
    if operator == "+":
        for arg in rest_of_args:
            result += arg
    elif operator == "-":
        for arg in rest_of_args:
            result -= arg
    elif operator == "*":
        for arg in rest_of_args:
            result *= arg
    elif operator == "/":
        for arg in rest_of_args:
            result /= arg
    return result
