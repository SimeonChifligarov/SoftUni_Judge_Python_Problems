nums = [int(el) for el in input().split(', ')]

positive_nums = [n for n in nums if n >= 0]
negative_nums = [n for n in nums if n < 0]
even_nums = [n for n in nums if n % 2 == 0]
odd_nums = [n for n in nums if not n % 2 == 0]

print(f'Positive: {", ".join([str(el) for el in positive_nums])}')
print(f'Negative: {", ".join([str(el) for el in negative_nums])}')
print(f'Even: {", ".join([str(el) for el in even_nums])}')
print(f'Odd: {", ".join([str(el) for el in odd_nums])}')
