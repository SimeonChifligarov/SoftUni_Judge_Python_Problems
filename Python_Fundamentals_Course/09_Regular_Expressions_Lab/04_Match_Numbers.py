import re

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"

numbers = input()
valid_numbers = re.finditer(pattern, numbers)

for valid_number in valid_numbers:
    if valid_number.group().startswith('00'):
        continue
    print(f"{valid_number.group()}", end=" ")
