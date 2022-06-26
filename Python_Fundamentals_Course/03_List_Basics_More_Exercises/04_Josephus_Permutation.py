# You are now to create a program that prints a Josephus permutation, receiving two lines of code (the list itself (string with elements separated by a single space) and a number k) as if they were in a circle and counted out every k places until none remained.

the_list_itself = [int(el) for el in input().split()]
number_k = int(input())
result = []
current_list = the_list_itself.copy()

for _ in range(len(the_list_itself)):
    new_number_k = number_k
    while new_number_k > len(current_list):
        new_number_k -= len(current_list)
    else:
        result.append(current_list[new_number_k - 1])
        current_list.pop(new_number_k - 1)
        current_left = current_list[:new_number_k - 1]
        current_right = current_list[new_number_k - 1:]
        current_list = current_right + current_left

result = [str(el) for el in result]
print(f"[{','.join(result)}]")
