numbers_as_list = [int(num) for num in input().split()]

negative_numbers = [num for num in numbers_as_list if num < 0]
positive_numbers = [num for num in numbers_as_list if num > 0]

print(sum(negative_numbers))
print(sum(positive_numbers))

if abs(sum(negative_numbers)) > sum(positive_numbers):
    print("The negatives are stronger than the positives")
elif abs(sum(negative_numbers)) < sum(positive_numbers):
    print("The positives are stronger than the negatives")
