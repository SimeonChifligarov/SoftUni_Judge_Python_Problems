# You will be given a number n. On the next n lines you will receive integers. You have to create and print two lists:
# •	One with all the positives (including 0) numbers
# •	One with all the negatives numbers
# Finally print the following message: "Count of positives: {count_positives}. Sum of negatives: {sum_of_negatives}"

number = int(input())
list_of_positives = []
list_of_negatives = []

for _ in range(1, number + 1):
    current_number = int(input())
    if current_number >= 0:
        list_of_positives.append(current_number)
    else:
        list_of_negatives.append(current_number)

print(list_of_positives)
print(list_of_negatives)
print(f'Count of positives: {len(list_of_positives)}')
print(f'Sum of negatives: {sum(list_of_negatives)}')
