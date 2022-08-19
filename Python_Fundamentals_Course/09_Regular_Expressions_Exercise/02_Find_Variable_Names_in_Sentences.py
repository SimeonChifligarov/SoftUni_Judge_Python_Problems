import re

pattern = r"((?<= _)|(?<=^_))[a-zA-Z0-9]+\b"

line_data = input()
var_names = [el.group() for el in re.finditer(pattern, line_data)]

print(*var_names, sep=",")

# # Solution 2
# import re
#
# pattern = r"((?<= _)|(?<=^_))[a-zA-Z0-9]+\b"
# all_var_names = []
#
# line_data = input()
# var_names = [el.group() for el in re.finditer(pattern, line_data)]
# all_var_names.extend(var_names)
# print(*all_var_names, sep=",")
