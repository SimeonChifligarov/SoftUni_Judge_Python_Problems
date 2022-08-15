# For each word:
# •	the second and the last letter are switched (e.g. Hello becomes Holle)
# •	the first letter is replaced by its character code (e.g. H becomes 72)

secret_message_as_list = input().split()
final_message_as_list = []
for word in secret_message_as_list:
    word_digits = [char for char in word if char.isnumeric()]
    ascii_code = int("".join(word_digits))
    first_letter = chr(ascii_code)
    word = [char for char in word if char not in word_digits]
    word[0], word[-1] = word[-1], word[0]
    final_word = "".join(list(first_letter) + word)
    final_message_as_list.append(final_word)
print(*final_message_as_list, sep=" ")
