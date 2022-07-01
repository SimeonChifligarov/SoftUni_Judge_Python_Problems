# Write a program that receives a single string and on the first line prints all the digits,
# on the second – all the letters, and on the third – all the other characters.
# There will always be at least one digit, one letter and one other characters.

string = input()

all_digits = ""
all_letters = ""
all_others = ""

for char in string:
    if char.isdigit():
        all_digits += char
    elif char.isalpha():
        all_letters += char
    elif not char.isalnum():
        all_others += char

print(all_digits)
print(all_letters)
print(all_others)
