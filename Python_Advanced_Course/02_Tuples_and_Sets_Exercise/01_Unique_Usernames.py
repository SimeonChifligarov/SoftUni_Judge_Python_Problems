unique_usernames = set()

number_of_usernames = int(input())

for _ in range(number_of_usernames):
    username = input()
    unique_usernames.add(username)

print(*unique_usernames, sep="\n")
