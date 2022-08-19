import re

data_as_line = input()
target_word = input()
pattern = fr"\b{target_word}\b"

target_word_lists = re.findall(pattern, data_as_line, re.IGNORECASE)
print(len(target_word_lists))
