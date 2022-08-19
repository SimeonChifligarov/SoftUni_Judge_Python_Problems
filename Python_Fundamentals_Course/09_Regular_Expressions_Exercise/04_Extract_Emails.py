import re

pattern = r"(^|(?<=\s))[a-zA-Z0-9]+([\._-][a-zA-Z0-9]+)?@[a-zA-Z]+(-[a-zA-Z]+)?(\.[a-zA-Z]+(-[a-zA-Z]+)?)+"

data_as_line = input()
all_emails = [el.group() for el in re.finditer(pattern, data_as_line)]
for email in all_emails:
    print(email)
