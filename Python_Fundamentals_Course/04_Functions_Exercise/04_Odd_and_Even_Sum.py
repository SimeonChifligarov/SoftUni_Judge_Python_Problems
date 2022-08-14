# You will receive a single number. You have to write a function that returns
# the sum of all even and all odd digits from that number as a single string
# like in the examples below.

def sum_of_even_and_odd_digits(num):
    num_as_string = str(num)
    even_sum = 0
    odd_sum = 0
    for char in num_as_string:
        if int(char) % 2 == 0:
            even_sum += int(char)
        else:
            odd_sum += int(char)
    return [odd_sum, even_sum]


number = int(input())
result = sum_of_even_and_odd_digits(number)
odd_sum = result[0]
even_sum = result[1]
print(f'Odd sum = {odd_sum}, Even sum = {even_sum}')

# # Solution 2
# def sum_of_even_and_odd_digits(num):
#     num_as_string = str(num)
#     even_sum = 0
#     odd_sum = 0
#     for index in range(len(num_as_string)):
#         if int(num_as_string[index]) % 2 == 0:
#             even_sum += int(num_as_string[index])
#         else:
#             odd_sum += int(num_as_string[index])
#     return print(f'Odd sum = {odd_sum}, Even sum = {even_sum}')
#
#
# number = int(input())
# sum_of_even_and_odd_digits(number)
