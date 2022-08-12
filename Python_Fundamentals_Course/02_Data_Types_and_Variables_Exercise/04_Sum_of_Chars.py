# Write a program, which sums the ASCII codes of n characters and prints the sum on the console.
# Input
# •	On the first line, you will receive n – the number of lines, which will follow
# •	On the next n lines – you will receive letters from the Latin alphabet

number_of_lines = int(input())
the_ascii_sum = 0

for number in range(number_of_lines):
    current_letter = input()
    the_ascii_sum += ord(current_letter)

print(f"The sum equals: {the_ascii_sum}")
