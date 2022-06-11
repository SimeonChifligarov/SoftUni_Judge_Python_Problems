from collections import deque

names_of_kids = input().split()
tossing_number = int(input())

kids_left = deque(names_of_kids)

while len(kids_left) > 1:
    kids_left.rotate(-tossing_number + 1)
    kid_out = kids_left.popleft()
    print(f"Removed {kid_out}")

last_kid = kids_left.popleft()
print(f"Last is {last_kid}")
