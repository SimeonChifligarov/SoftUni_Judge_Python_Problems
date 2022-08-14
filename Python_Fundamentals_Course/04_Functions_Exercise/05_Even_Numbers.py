# # Solution 1
# nums = [int(el) for el in input().split()]
# even_nums = [num for num in nums if num % 2 == 0]
# print(even_nums)

# Solution 2 -> 'Use filter()'

nums = [int(el) for el in input().split()]
even_numbers = filter(lambda num: num % 2 == 0, nums)
print(list(even_numbers))
