# Read four integer numbers. Add first to the second, divide (integer) the sum by the third number
# and multiply the result by the fourth number. Print the result.

number_one = int(input())
number_two = int(input())
number_three = int(input())
number_four = int(input())

result = int((number_one + number_two) / number_three) * number_four
print(f'{result}')
