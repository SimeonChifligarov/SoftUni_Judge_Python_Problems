numbers = [float(el) for el in input().split()]

number_counts_as_dict = {}

for number in numbers:
    if number not in number_counts_as_dict:
        number_counts_as_dict[number] = 0
    number_counts_as_dict[number] += 1

for num in number_counts_as_dict:
    print(f"{num} - {number_counts_as_dict[num]} times")
