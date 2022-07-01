# On the first line you will receive a string. On the second line you will receive a second string.
# Write a program that removes all the occurrences of the first string in the second until there is no match.
# At the end print the remaining string.

to_be_removed = input()
string = input()

while to_be_removed in string:
    string = string.replace(to_be_removed, "")
print(string)
