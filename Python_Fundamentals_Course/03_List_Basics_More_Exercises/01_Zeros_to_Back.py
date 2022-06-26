# Write a program that receives a single string (integers separated by a comma and space ", "), finds all the zeros
# and moves them to the back without messing up the other elements. Print the resulting integer list

integers_as_list = [int(num) for num in input().split(", ")]

zeros = integers_as_list.count(0)
zeros_list = [0] * zeros
integers_with_no_zeros = [num for num in integers_as_list if not num == 0]
final_list = integers_with_no_zeros + zeros_list
print(final_list)
