# You will receive a field of a tic-tac-toe game in three lines containing numbers separated by a single space.
# Legend:
# •	0 - empty space
# •	1 - first player move
# •	2 - second player move

line_one = input().split()
line_two = input().split()
line_three = input().split()

diagonal_one = [line_one[0], line_two[1], line_three[2]]
diagonal_two = [line_one[2], line_two[1], line_three[0]]

column_one = [line_one[0], line_two[0], line_three[0]]
column_two = [line_one[1], line_two[1], line_three[1]]
column_three = [line_one[2], line_two[2], line_three[2]]

if set(line_one) == set("1") or set(line_two) == set("1") or set(line_three) == set("1") or set(diagonal_one) == set(
        "1") or set(diagonal_two) == set("1") or set(column_one) == set("1") or set(column_two) == set("1") or set(
    column_three) == set("1"):
    print("First player won")
elif set(line_one) == set("2") or set(line_two) == set("2") or set(line_three) == set("2") or set(diagonal_one) == set(
        "2") or set(diagonal_two) == set("2") or set(column_one) == set("2") or set(column_two) == set("2") or set(
    column_three) == set("2"):
    print("Second player won")
else:
    print("Draw!")
