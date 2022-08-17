# You will be receiving lines in the following format: "{username}-{language}-{points}" until you receive
# "exam finished". You should store each username and his submissions and points.

data = input()
users_results = {}
languages = {}

while not data == "exam finished":
    split_data = data.split("-")
    username = split_data[0]
    command = split_data[1]
    points = 0
    if len(split_data) > 2:
        points = int(split_data[2])

    if not command == "banned":
        if username in users_results:
            if users_results[username] < points:
                users_results[username] = points
        else:
            users_results[username] = points
        if command not in languages:
            languages[command] = 0
        languages[command] += 1

    else:
        users_results.pop(username)

    data = input()

# sorted_users_results = sorted(users_results.items(), key=lambda x: (-x[1], x[0]))
# print("Results:")
# for user, res in sorted_users_results:
#     print(f"{user} | {res}")
#
# sorted_languages = sorted(languages.items(), key=lambda x: (-x[1], x[0]))
# print("Submissions:")
# for lang, count in sorted_languages:
#     print(f"{lang} - {count}")

print("Results:")
for user, res in users_results.items():
    print(f"{user} | {res}")

print("Submissions:")
for lang, count in languages.items():
    print(f"{lang} - {count}")
