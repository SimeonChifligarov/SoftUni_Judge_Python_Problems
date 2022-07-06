from collections import deque

substrings = deque(input().split())

# print(substrings)

main_colors = ['red', 'yellow', 'blue']
secondary_colors_as_dict = {'orange': ['red', 'yellow'],
                            'purple': ['red', 'blue'],
                            'green': ['yellow', 'blue']
                            }

result = []

while len(substrings) > 1:
    start_substr = substrings[0]
    end_substr = substrings[-1]

    current_result = start_substr + end_substr
    if (current_result in main_colors) or (current_result in secondary_colors_as_dict):
        result.append(current_result)
        substrings.popleft()
        substrings.pop()
        continue

    current_result_reverse = end_substr + start_substr
    if (current_result_reverse in main_colors) or (current_result_reverse in secondary_colors_as_dict):
        result.append(current_result_reverse)
        substrings.popleft()
        substrings.pop()
    else:
        substrings.popleft()
        substrings.pop()
        position_to_insert = len(substrings) // 2
        if len(end_substr) > 1:
            substrings.insert(position_to_insert, end_substr[:-1])
        if len(start_substr) > 1:
            substrings.insert(position_to_insert, start_substr[:-1])

if len(substrings) == 1:
    el = substrings[0]
    if el in main_colors or el in secondary_colors_as_dict:
        result.append(el)

if not ('red' in result and 'yellow' in result):
    result = [el for el in result if not el == 'orange']
if not ('red' in result and 'blue' in result):
    result = [el for el in result if not el == 'purple']
if not ('yellow' in result and 'blue' in result):
    result = [el for el in result if not el == 'green']

print(result)
