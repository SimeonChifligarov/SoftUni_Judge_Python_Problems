def palindrome(word, index=0):
    left_letter = word[index]
    right_letter = word[len(word) - 1 - index]

    if index >= len(word) - 1 - index:
        return f"{word} is a palindrome"

    if not left_letter == right_letter:
        return f"{word} is not a palindrome"
    return palindrome(word, index + 1)

#
# print(palindrome("abcba", 0))
# print(palindrome("peter", 0))
# print(palindrome("a", 0))
# print(palindrome("bb", 0))
# print(palindrome("prostominaotsorp", 0))
#

# # Solution 2 - not by requirements
#
# def palindrome(word, index):
#     if word == word[::-1]:
#         return f"{word} is a palindrome"
#     return f"{word} is not a palindrome"
#
# #
# # print(palindrome("abcba", 0))
# # print(palindrome("peter", 0))
