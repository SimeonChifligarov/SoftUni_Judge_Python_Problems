# using dictionary comprehension

chars_and_ascii_dict = {ch: ord(ch) for ch in input().split(', ')}
print(chars_and_ascii_dict)

# # Solution 2
# list_of_chars = [ch for ch in input().split(', ')]
#
# chars_and_ascii_dict = {}
#
# for ch in list_of_chars:
#     if ch not in chars_and_ascii_dict:
#         chars_and_ascii_dict[ch] = ord(ch)
#
# print(chars_and_ascii_dict)
