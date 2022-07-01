starting_char = input()
ending_char = input()
random_string = input()

starting_index = ord(starting_char)
ending_index = ord(ending_char)
total_sum = 0

for char in random_string:
    if ord(char) in range(starting_index + 1, ending_index):
        total_sum += ord(char)
print(total_sum)
