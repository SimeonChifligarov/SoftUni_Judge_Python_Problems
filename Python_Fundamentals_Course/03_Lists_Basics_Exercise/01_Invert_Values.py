numbers_as_list = [int(num) for num in input().split()]

final_list = [-num for num in numbers_as_list]

print(final_list)

# # Solution 2
# # Write a program that receives a single string containing numbers separated by a single space.
# # Print a list containing the opposite of each number.
#
# reversed_list = []
# string_of_numbers = input()
# original_list = string_of_numbers.split()
# for n in original_list:
#     reversed_list.append(-int(n))
# print(reversed_list)
