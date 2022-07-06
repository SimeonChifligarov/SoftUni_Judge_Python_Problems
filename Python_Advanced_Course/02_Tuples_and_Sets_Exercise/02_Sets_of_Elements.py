length_of_sets = [int(el) for el in input().split()]

set_one = set()
set_one_length = length_of_sets[0]

set_two = set()
set_two_length = length_of_sets[1]

for _ in range(set_one_length):
    number = int(input())
    set_one.add(number)

for _ in range(set_two_length):
    number = int(input())
    set_two.add(number)

set_intersection = set_one.intersection(set_two)

print(*set_intersection, sep='\n')
