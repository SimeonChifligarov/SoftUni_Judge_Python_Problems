# You will be given series of strings until you receive an "end" command.
# Write a program that reverses strings and prints each pair on separate line in format "{word} = {reversed word}".

data = input()

while not data == "end":
    print(f"{data} = {data[::-1]}")
    data = input()
