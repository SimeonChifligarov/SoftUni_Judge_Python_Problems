# Given a number, print the largest number that can be formed from the digits of the given number.

number = input()

number_as_list = [int(digit) for digit in number]
number_as_list.sort(reverse=True)
print(*number_as_list, sep="")

# # Solution 2
# number_as_string = input()
#
# number_list = []
# for i in range(len(number_as_string)):
#     number_list.append(int(number_as_string[i]))
# number_list.sort(reverse=True)
#
# print(*number_list, sep="")
