# Find online more information about ASCII (American Standard Code for Information Interchange)
# and write a program that prints part of the ASCII table of characters on the console.
# On the first line of input you will receive the char index you should start with and on the second line -
# the index of the last character you should print.

starting_char_index = int(input())
last_char_index = int(input())

for index in range(starting_char_index, last_char_index + 1):
    print(f"{chr(index)}", end=" ")

# # Solution 2
# starting_char = int(input())
# finishing_char = int(input())
#
# for i in range(starting_char, finishing_char + 1):
#     print(chr(i), end=' ')
