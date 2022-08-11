# # Solution 1
# starting_string = input()
# finished_string = input()
#
# previous_string = starting_string
# current_string = ""
#
# for index in range(len(starting_string)):
#     for j in range(index + 1):
#         current_string += finished_string[j]
#     for k in range(index + 1, len(starting_string)):
#         current_string += starting_string[k]
#     if not current_string == previous_string:
#         print(current_string)
#     previous_string = current_string
#     current_string = ""
#

# Solution 2
# You will be given two strings. Transform the first string into the second one, one letter at a time and print it.
# Print only the unique strings
# Note: the strings will have the same lengths

first_string = input()
second_string = input()

first_string_as_list = [char for char in first_string]
second_string_as_list = [char for char in second_string]

for index in range(len(first_string_as_list)):
    if first_string_as_list[index] == second_string_as_list[index]:
        continue
    else:
        first_string_as_list[index] = second_string_as_list[index]
        print(''.join(first_string_as_list))
