# Write a function that receives an integer number and returns if this number is perfect or NOT.
# A perfect number is a positive integer that is equal to the sum of its proper positive divisors.
# That is the sum of its positive divisors excluding the number itself (also known as its aliquot sum).

def is_perfect_number(num):
    list_of_divisors = []
    for n in range(1, int((num / 2)) + 1):
        if num % n == 0:
            list_of_divisors.append(n)
    if sum(list_of_divisors) == num:
        return True
    return False


number = int(input())
if is_perfect_number(number):
    print('We have a perfect number!')
else:
    print('It\'s not so perfect.')
