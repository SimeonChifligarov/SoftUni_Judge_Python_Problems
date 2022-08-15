previous_version = input().split(".")
previous_version_as_num = int("".join(previous_version))
current_version_as_num = previous_version_as_num + 1
current_version_as_list = list(str(current_version_as_num))
print(".".join(current_version_as_list))
