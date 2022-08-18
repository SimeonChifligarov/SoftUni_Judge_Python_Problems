data = input()
result = ""
total_strength = 0
index = -1
for char in data:
    index += 1
    if char == ">":
        result += ">"
        total_strength += int(data[index + 1])
    elif not total_strength == 0:
        total_strength -= 1
    else:
        result += char

print(result)
