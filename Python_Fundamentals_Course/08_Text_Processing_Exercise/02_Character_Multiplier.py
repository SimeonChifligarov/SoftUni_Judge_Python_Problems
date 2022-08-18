word_one, word_two = input().split()

min_len = min(len(word_one), len(word_two))
total_result = 0

for index in range(min_len):
    total_result += ord(word_one[index]) * ord(word_two[index])

if len(word_one) > len(word_two):
    for index in range(min_len, len(word_one)):
        total_result += ord(word_one[index])
else:
    for index in range(min_len, len(word_two)):
        total_result += ord(word_two[index])

print(total_result)
