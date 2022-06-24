# You will receive a number that represents the highest number of stars.

number = int(input())

for i in range(1, number + 1):
    print(f'*' * i)
for j in range(number - 1, 0, -1):
    print(f'*' * j)
