# A palindrome is a number which reads the same backward as forward, such as 323 or 1001.
# Write a function which receives a list of positive integers and checks if each integer
# is a palindrome or not. Print the results on the console
# The input will be a single string containing the numbers separated by comma and space ", "

def check_if_word_is_palindrome(word):
    if word == word[::-1]:
        return True
    return False


list_of_numbers = input().split(", ")
for number in list_of_numbers:
    print(check_if_word_is_palindrome(number))

# # Solution 2
# def check_if_word_is_palindrome(word):
#     word = str(word)
#     if word == word[::-1]:
#         return True
#     return False
#
#
# list_of_numbers = input().split(", ")
# for number in list_of_numbers:
#     print(check_if_word_is_palindrome(number))
