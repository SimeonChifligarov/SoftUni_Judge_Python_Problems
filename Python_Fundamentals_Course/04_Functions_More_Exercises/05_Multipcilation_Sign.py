# You are given a number num1, num2 and num3. Write a program that finds if num1 * num2 * num3
# (the product) is negative, positive or zero. Try to do this WITHOUT multiplying the 3 numbers.

num1 = float(input())
num2 = float(input())
num3 = float(input())

all_numbers = [num1, num2, num3]
negative_numbers = [num for num in all_numbers if num < 0]

if all_numbers.count(0) >= 1:
    print("zero")
elif len(negative_numbers) % 2 == 0:
    print("positive")
else:
    print("negative")
