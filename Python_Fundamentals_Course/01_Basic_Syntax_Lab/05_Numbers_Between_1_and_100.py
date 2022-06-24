# Write a program which reads numbers from the console until it receives a number between 1 and 100 inclusive.
# When the correct number is received, stop reading and print "The number {number} is between 1 and 100"

current_number = float(input())
while current_number > 100 or current_number < 1:
    current_number = float(input())

print(f'The number {current_number} is between 1 and 100')
