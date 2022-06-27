# You are given the coordinates of two points on a Cartesian coordinate system - X1, Y1, X2 and Y2.
# Create a method that prints the point that is closest to the center of the coordinate system (0, 0)
# in the format (X, Y). If the points are on a same distance from the center, print only the first one.
# The resulting coordinates must be formatted to the lowest integer

import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

if x1 ** 2 + y1 ** 2 <= x2 ** 2 + y2 ** 2:
    print(f'({math.floor(x1)}, {math.floor(y1)})')
else:
    print(f'({math.floor(x2)}, {math.floor(y2)})')
