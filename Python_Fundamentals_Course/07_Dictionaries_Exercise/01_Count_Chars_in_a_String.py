# Write a program that counts all characters in a string except for space (' ').
# Print all the occurrences in the following format:
# {char} -> {occurrences}

data = input()

occurrences_dict = {}

for char in data:
    if not char == " ":
        if char not in occurrences_dict:
            occurrences_dict[char] = 0
        occurrences_dict[char] += 1

for occur, count in occurrences_dict.items():
    print(f"{occur} -> {count}")

# # Solution 2
# data = input()
# data_without_spaces = [char for char in data if not char == " "]
#
# occurrences_dict = {}
#
# for char in data_without_spaces:
#     if char not in occurrences_dict:
#         occurrences_dict[char] = 0
#     occurrences_dict[char] += 1
#
# for occur, count in occurrences_dict.items():
#     print(f"{occur} -> {count}")
