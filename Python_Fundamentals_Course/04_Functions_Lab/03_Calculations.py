# Create a function that receives three parameters and calculates a result depending on operator. The operator can be  'multiply', 'divide', 'add', 'subtract' . The input comes as three parameters – two integers and an operator as a string.

def calculation_with_operator(int1, int2, operator):
    result = None
    if operator == "multiply":
        result = int1 * int2
    elif operator == "divide":
        result = int(int1 / int2)
    elif operator == "add":
        result = int1 + int2
    elif operator == "subtract":
        result = int1 - int2
    return result


operator_data = input()
a = int(input())
b = int(input())

print(calculation_with_operator(a, b, operator_data))
