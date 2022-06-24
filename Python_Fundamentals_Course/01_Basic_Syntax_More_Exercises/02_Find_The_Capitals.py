# Write a program that takes a single string and prints a list of all the indices of all the capital letters.

sting = input()
indices_list = []

for index in range(len(sting)):
    if sting[index].isupper():
        indices_list.append(index)

print(indices_list)
