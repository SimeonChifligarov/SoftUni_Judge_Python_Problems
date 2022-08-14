# You will receive three integer numbers.
# Write a function sum_numbers() to get the sum of the first two integers and subtract() function that subtracts the third integer from the result. Wrap the two functions in a function called add_and_subtract() which will receive the three numbers

def sum_numbers(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def add_and_subtract(num1, num2, num3):
    return subtract((sum_numbers(num1, num2)), num3)


a = int(input())
b = int(input())
c = int(input())
print(add_and_subtract(a, b, c))

# # Solution 0
# a = int(input())
# b = int(input())
# c = int(input())
#
# print(a+b-c)
#
