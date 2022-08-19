import re

pattern = r"\bw{3}\.[a-zA-Z0-9-]+(\.[a-z]+)+"
all_emails = []

current_line = input()

while current_line:
    current_emails = [el.group() for el in re.finditer(pattern, current_line)]
    all_emails.extend(current_emails)
    current_line = input()

for email in all_emails:
    print(email)

# # Solution 2
# import re
#
# pattern = r"\bw{3}\.[a-zA-Z0-9-]+(\.[a-z]+)+"
#
# current_line = input()
#
# while current_line:
#     current_emails = [el.group() for el in re.finditer(pattern, current_line)]
#     if current_emails:
#         print(*current_emails, sep="\n")
#     current_line = input()
