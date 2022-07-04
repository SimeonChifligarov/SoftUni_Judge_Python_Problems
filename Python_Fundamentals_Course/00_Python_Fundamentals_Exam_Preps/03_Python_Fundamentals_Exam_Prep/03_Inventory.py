# You will receive a journal with some Collecting items, separated with ', ' (comma and space). After that, until receiving "Craft!" you will be receiving different commands.
# Commands (split by " - "):

journal_with_items = input().split(', ')

command_as_whole = input()

while not command_as_whole == "Craft!":
    current_command = command_as_whole.split(' - ')
    real_command = current_command[0]
    item = current_command[1]
    if real_command == "Collect":
        if item not in journal_with_items:
            journal_with_items.append(item)
    elif real_command == "Drop":
        if item in journal_with_items:
            journal_with_items.remove(item)
    elif real_command == "Combine Items":
        combined_items = item.split(":")
        if combined_items[0] in journal_with_items:
            journal_with_items.insert(journal_with_items.index(combined_items[0]) + 1, combined_items[1])
    elif real_command == "Renew":
        if item in journal_with_items:
            journal_with_items.remove(item)
            journal_with_items.append(item)
    command_as_whole = input()

print(*journal_with_items, sep=", ")
