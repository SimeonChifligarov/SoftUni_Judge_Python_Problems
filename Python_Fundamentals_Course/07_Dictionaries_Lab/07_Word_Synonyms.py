# The key of the dictionary will be the word. The value will be a list of all the synonyms of that word.
# You will be given a number n – the count of the words. After each word, you will be given a synonym,
# so the count of lines you have to read from the console is 2 * n.

count_of_words = int(input())

dictionary = {}

for _ in range(count_of_words):
    word = input()
    synonym = input()
    if word not in dictionary:
        dictionary[word] = []
    dictionary[word].append(synonym)

for word, list_of_synonyms in dictionary.items():
    print(f"{word} - {', '.join(list_of_synonyms)}")
