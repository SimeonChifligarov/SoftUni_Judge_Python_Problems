# Write a program that reads a floating-point number and prints "zero" if the number is zero.
# Otherwise, print "positive" or "negative". Add "small" if the absolute value of the number is less than 1,
# or "large" if it exceeds 1 000 000.

number = float(input())

if number == 0:
    print('zero')
elif number < 0:
    if -1 < number:
        print('small negative')
    elif -1000000 < number:
        print('negative')
    else:
        print('large negative')
else:
    if number < 1:
        print('small positive')
    elif number < 1000000:
        print('positive')
    else:
        print('large positive')
