# Write a program that receives on the first line words separated by a space and a searched palindrome on the second.
# Print all the palindromes on the first line. Print all the occurrences of the searched palindrome in the format:
# "Found palindrome {count} times"

words = input().split()
searched_palindrome = input()
# all_palindromes = [word for word in words if word == word[::-1]]
all_palindromes = []
for word in words:
    if word == "".join(reversed(word)):
        all_palindromes.append(word)

print(all_palindromes)
print(f'Found palindrome {all_palindromes.count(searched_palindrome)} times')

# # Solution 2
#
# words = input().split()
# searched_palindrome = input()
#
# all_palindromes = [word for word in words if word == word[::-1]]
# print(all_palindromes)
# print(f'Found palindrome {all_palindromes.count(searched_palindrome)} times')


# # Solution 3
#
# words = input().split()
# searched_palindrome = input()
#
# all_palindromes = [word for word in words if word == word[::-1]]
# print(all_palindromes)
# count = 0
# for word in all_palindromes:
#     if word == searched_palindrome:
#         count += 1
# print(f'Found palindrome {count} times')
