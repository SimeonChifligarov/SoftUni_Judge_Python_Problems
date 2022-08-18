data = input().split(", ")

for word in data:
    invalid_chars = 0
    if len(word) > 16 or len(word) < 3:
        continue
    for char in word:
        if not (char.isalnum() or char == "_" or char == "-"):
            invalid_chars += 1
            break
    if not invalid_chars:
        print(word)
