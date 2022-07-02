participants = input().split(", ")

scores = {}
for participant in participants:
    scores[participant] = 0

text = input()

while not text == "end of race":
    current_name = ""
    current_score = 0
    for char in text:
        if char.isalpha():
            current_name += char
        elif char.isdigit():
            current_score += int(char)

    if current_name in participants:
        scores[current_name] += current_score
    text = input()

sorted_scores = sorted(scores.items(), key=lambda x: -x[1])

print(f"1st place: {sorted_scores[0][0]}")
print(f"2nd place: {sorted_scores[1][0]}")
print(f"3rd place: {sorted_scores[2][0]}")
