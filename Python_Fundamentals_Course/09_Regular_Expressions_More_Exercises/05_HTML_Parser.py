import re

title_pattern = r"(?<=<title>).+(?=</title>)"
body_pattern = r"(?<=<body>).+(?=</body)"
tags_pattern = r"<[^>]+>"
new_line_patter = r"\\n|\\t|\\r"

all_data = input()

title = re.findall(title_pattern, all_data)
title = ''.join(title)
title_a = re.split(new_line_patter, title)
print(f"Title: {''.join(title_a)}")

body = [el.group() for el in re.finditer(body_pattern, all_data)]

final_body = re.split(tags_pattern, *body)
final_text = ''.join(final_body)
final_text_a = re.split(new_line_patter, final_text)
print(f"Content: {''.join(final_text_a)}")
