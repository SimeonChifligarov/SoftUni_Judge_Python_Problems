string = input()

for index in range(len(string) - 1):
    if string[index] == ":":
        print(f":{string[index + 1]}")

# # Solution 2
# string = input()
#
# for index in range(len(string) - 1):
#     if string[index] == ":":
#         print(f"{string[index]}{string[index + 1]}")
