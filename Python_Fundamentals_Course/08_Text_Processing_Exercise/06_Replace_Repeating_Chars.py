string = input()
string_as_list = list(string)
for index in range(len(string) - 1, 0, -1):
    if string[index] == string[index - 1]:
        string_as_list.pop(index)
print(*string_as_list, sep="")

# # Solution 2
# string = input()
#
# for index in range(len(string) - 1, 0, -1):
#     if string[index] == string[index - 1]:
#         string = string[:index - 1] + string[index:]
# print(string)
