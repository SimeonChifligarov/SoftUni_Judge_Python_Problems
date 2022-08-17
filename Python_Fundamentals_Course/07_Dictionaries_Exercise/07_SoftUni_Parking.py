# •	First line: n - number of commands - integer
# •	Next n lines: commands in one of the two possible formats:
# o	Register: "register {username} {licensePlateNumber}"
# o	Unregister: "unregister {username}"

number_of_commands = int(input())
registered_dict = {}

for _ in range(number_of_commands):
    full_command_list = input().split()
    command = full_command_list[0]
    if command == "register":
        name = full_command_list[1]
        plate_number = full_command_list[2]
        if name not in registered_dict:
            registered_dict[name] = plate_number
            print(f"{name} registered {registered_dict[name]} successfully")
        else:
            print(f"ERROR: already registered with plate number {registered_dict[name]}")
    elif command == "unregister":
        name = full_command_list[1]
        if name in registered_dict:
            print(f"{name} unregistered successfully")
            registered_dict.pop(name)
        else:
            print(f"ERROR: user {name} not found")

for username, plate in registered_dict.items():
    print(f"{username} => {plate}")
