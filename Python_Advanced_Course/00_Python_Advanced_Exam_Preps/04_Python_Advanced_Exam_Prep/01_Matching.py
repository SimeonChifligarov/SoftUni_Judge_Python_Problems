from collections import deque

males = deque([int(el) for el in input().split()])
females = deque([int(el) for el in input().split()])

matches = 0

while males and females:
    current_female = females[0]
    current_male = males[-1]

    if current_female <= 0:
        females.popleft()
        continue

    if current_male <= 0:
        males.pop()
        continue

    if current_female % 25 == 0:
        females.popleft()
        females.popleft()
        continue

    if current_male % 25 == 0:
        males.pop()
        males.pop()
        continue

    if current_female == current_male:
        females.popleft()
        males.pop()
        matches += 1
    else:
        males[-1] -= 2
        females.popleft()

print(f"Matches: {matches}")

print(f"Males left: {', '.join([str(el) for el in males][::-1]) if males else 'none'}")
print(f"Females left: {', '.join([str(el) for el in females]) if females else 'none'}")
