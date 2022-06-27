# You are given the coordinates of four points in the 2D plane.
# The first and the second pair of points form two different lines.
# Print the longer line in format "(X1, Y1)(X2, Y2)" starting with the point
# that is closer to the center of the coordinate system (0, 0)
# (You can reuse the method that you wrote for the previous problem).
# If the lines are of equal length, print only the first one.
# The resulting coordinates must be formatted to the lowest integer.

import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

if (max(x1, x2) - min(x1, x2)) ** 2 + (max(y1, y2) - min(y1, y2)) ** 2 >= (max(x3, x4) - min(x3, x4)) ** 2 + (
        max(y3, y4) - min(y3, y4)) ** 2:
    z1 = x1
    z2 = y1
    z3 = x2
    z4 = y2
else:
    z1 = x3
    z2 = y3
    z3 = x4
    z4 = y4

if z1 ** 2 + z2 ** 2 <= z3 ** 2 + z4 ** 2:
    print(f'({math.floor(z1)}, {math.floor(z2)})({math.floor(z3)}, {math.floor(z4)})')
else:
    print(f'({math.floor(z3)}, {math.floor(z4)})({math.floor(z1)}, {math.floor(z2)})')
