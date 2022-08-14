# Write a function which receives three integer numbers and returns the smallest. Use appropriate name for the function.

def min_of_three(num1, num2, num3):
    return min(num1, num2, num3)


a = int(input())
b = int(input())
c = int(input())
print(min_of_three(a, b, c))
