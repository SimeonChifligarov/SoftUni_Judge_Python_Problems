# Write a program to check if a number is prime (only wholly divisible by itself and one).
# The input comes as an integer number.
# The output should be true for prime number and false otherwise.

number = int(input())

is_prime = True

for divisor in range(2, int(number / 2) + 1):
    if number % divisor == 0:
        is_prime = False
        break

print(is_prime)
