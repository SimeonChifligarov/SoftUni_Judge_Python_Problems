# Write a function that receives two integer numbers.
# Calculate factorial of each number. Divide the first result by the second and
# print the division formatted to the second decimal point.

def factorial_of_num(num):
    result = 1
    for num in range(1, num + 1):
        result *= num
    return result


first_number = int(input())
second_number = int(input())

first_number_factorial = factorial_of_num(first_number)
second_number_factorial = factorial_of_num(second_number)

print(f'{first_number_factorial / second_number_factorial :.2f}')

# # Solution 2
# import math
#
# a = int(input())
# b = int(input())
#
# print(f'{math.factorial(a) / math.factorial(b):.2f}')
