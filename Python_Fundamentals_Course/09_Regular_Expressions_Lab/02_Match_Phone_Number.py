import re

phone_numbers = input()
pattern = r"(^|(?<=\s))\+359( |-)2\2\d{3}\2\d{4}\b"

valid_phone_numbers = [el.group() for el in re.finditer(pattern, phone_numbers)]
print(*valid_phone_numbers, sep=", ")
