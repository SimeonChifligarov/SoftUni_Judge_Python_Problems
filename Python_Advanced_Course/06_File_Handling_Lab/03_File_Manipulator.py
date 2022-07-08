import os

line = input()
while line != "End":
    command, *rest = line.split("-")

    if command == "Add":
        filename, line = rest
        with open(filename, "a") as file:
            file.write(line + "\n")

    elif command == "Replace":
        filename, old, new = rest

        try:
            with open(filename, "r") as file:
                content = file.read()

            with open(filename, "w") as file:
                content = content.replace(old, new)
                file.write(content)
        except Exception as e:
            print("An error occurred")
            line = input()
            continue

        print("replace")

    elif command == "Create":
        with open(rest[0], "w"):
            pass

    elif command == "Delete":
        try:
            os.remove(rest[0])
        except FileNotFoundError as e:
            print("An error occurred")

    line = input()