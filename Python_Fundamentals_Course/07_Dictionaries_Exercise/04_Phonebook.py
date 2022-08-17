phonebook = {}

while True:
    contact = input()

    if '-' not in contact:
        break

    contact_tokens = contact.split('-')

    phonebook[contact_tokens[0]] = contact_tokens[1]

for _ in range(int(contact)):
    name = input()
    if name not in phonebook:
        print(f'Contact {name} does not exist.')
    else:
        print(f'{name} -> {phonebook[name]}')
