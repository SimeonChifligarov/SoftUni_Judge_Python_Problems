#

# You will receive a single number n. On the next n lines you will receive integers. After that you will be given one of the following commands:

number = int(input())
list_of_numbers = []
list_of_filtered = []

for n in range(1, number + 1):
    current_number = int(input())
    list_of_numbers.append(current_number)

command = input()
# •	even
# •	odd
# •	negative
# •	positive
for n in list_of_numbers:
    if command == "even":
        if n % 2 == 0:
            list_of_filtered.append(n)
    elif command == "odd":
        if not n % 2 == 0:
            list_of_filtered.append(n)
    elif command == "negative":
        if n < 0:
            list_of_filtered.append(n)
    elif command == "positive":
        if n >= 0:
            list_of_filtered.append(n)
print(list_of_filtered)
