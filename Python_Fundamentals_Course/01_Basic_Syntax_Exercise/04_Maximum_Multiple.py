# Given a Divisor and a Bound, find the largest integer N, such that:
# N is divisible by divisor
# N is less than or equal to bound
# N is greater than 0.
# Notes: The divisor and bound are only positive values. It's guaranteed that a divisor is found

# # Solution 1
# divisor = int(input())
# bound = int(input())
#
# for n in range(bound, 0, -1):
#     if n % divisor == 0:
#         print(n)
#         break
#

# Solution 2
divisor = int(input())
bound = int(input())

current_number = bound

while not current_number % divisor == 0:
    current_number -= 1

print(current_number)
