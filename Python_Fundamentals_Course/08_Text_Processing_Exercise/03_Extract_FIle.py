file_location = input()
file_path = file_location.split("\\")
file_name_extension = file_path[-1]

name, extension = file_name_extension.split(".")
print(f"File name: {name}")
print(f"File extension: {extension}")
