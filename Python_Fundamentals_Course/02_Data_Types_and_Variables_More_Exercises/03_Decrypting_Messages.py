# •	On the first line, you will receive the key
# •	On the second line, you will receive n – the number of lines, which will follow
# •	On the next n lines – you will receive lower and uppercase characters from the Latin alphabet

key = int(input())
number_of_lines = int(input())
result = []

for _ in range(number_of_lines):
    char = input()
    result.append(chr(ord(char) + key))

print(''.join(result))
