data = input().upper()
current_string = ""
total_string = ""
number_of_repeats = 0
index = -1
for char in data:
    index += 1
    if not char.isdigit():
        current_string += char
    else:
        if index + 1 in range(len(data)):
            if data[index + 1].isdigit():
                number_of_repeats = 10 * int(data[index]) + int(data[index + 1])
            else:
                number_of_repeats = int(data[index])
            current_string *= number_of_repeats
            total_string += current_string
            current_string = ""
            number_of_repeats = 0
        else:
            number_of_repeats = int(data[index])
            current_string *= number_of_repeats
            total_string += current_string
print(f"Unique symbols used: {len(set(total_string))}")
print(total_string)
