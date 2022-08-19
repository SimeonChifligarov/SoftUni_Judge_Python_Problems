import re

pattern = r"\d+"
all_numbers = []

line_data = input()

while line_data:
    all_digits = re.findall(pattern, line_data)
    all_numbers.extend(all_digits)
    line_data = input()

print(*all_numbers)
