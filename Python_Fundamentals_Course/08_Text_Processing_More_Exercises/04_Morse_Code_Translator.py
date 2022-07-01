morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
              ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
alphabet = [chr(96 + num).upper() for num in range(1, 27)]
dict_morse_to_alpha = {morse_code[i]: alphabet[i] for i in range(len(morse_code))}

data = input()
chars = data.split()

result = ""
for char in chars:
    if char == "|":
        result += " "
    else:
        result += dict_morse_to_alpha[char]
print(result)
