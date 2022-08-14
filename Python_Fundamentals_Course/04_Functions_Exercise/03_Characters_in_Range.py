# Write a function that receives two characters and returns a single string with
# all the characters in between them according to the ASCII code.

def string_between_two_char(start, end):
    result = []
    for i in range(ord(start) + 1, ord(end)):
        result.append(chr(i))
    return result


char1 = input()
char2 = input()
print(" ".join(string_between_two_char(char1, char2)))
