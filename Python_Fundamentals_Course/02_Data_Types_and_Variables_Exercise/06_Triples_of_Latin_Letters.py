# Write a program to read an integer n and print all triples of the first n small Latin letters, ordered alphabetically:

n_letters = int(input())

for i in range(n_letters):
    for j in range(n_letters):
        for k in range(n_letters):
            print(f'{chr(i + 97)}{chr(j + 97)}{chr(k + 97)}')
