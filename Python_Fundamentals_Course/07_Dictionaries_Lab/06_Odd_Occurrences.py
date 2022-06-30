# Write a program that extracts all elements from a given sequence of words
# that are present in it an odd number of times (case-insensitive).
# •	Words are given on a single line, space separated.
# •	Print the result elements in lowercase, in their order of appearance.

seq_of_words = input().lower().split()

words_dict = {}

for word in seq_of_words:
    if word not in words_dict:
        words_dict[word] = 0
    words_dict[word] += 1

for word, count in words_dict.items():
    if not count % 2 == 0:
        print(word, end=" ")
