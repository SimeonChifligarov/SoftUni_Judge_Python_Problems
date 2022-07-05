#
import re

data_input = input()

pattern_potential = r"(@|#)(?P<word_one>[a-zA-Z]{3,})\1\1(?P<word_two>[a-zA-Z]{3,})\1"

real_matches = []
print_matches = []

matches_potential = [el for el in re.finditer(pattern_potential, data_input)]
all_matches = len(matches_potential)
for match in matches_potential:
    el_dict = match.groupdict()
    if el_dict['word_one'] == el_dict['word_two'][::-1]:
        real_matches.append(el_dict['word_one'])

if not all_matches:
    print("No word pairs found!")
else:
    print(f"{all_matches} word pairs found!")
if not real_matches:
    print("No mirror words!")
else:
    print("The mirror words are:")
    for word in real_matches:
        print_matches.append(f"{word} <=> {word[::-1]}")
    print(*print_matches, sep=", ")
