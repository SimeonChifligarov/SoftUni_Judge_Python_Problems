list_of_numbers = input().split()

stack = []

for _ in range(len(list_of_numbers)):
    stack.append(list_of_numbers.pop())

print(*stack)
