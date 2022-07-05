# Write a program to read a sequence of integers and find and print the top 5 numbers that are greater than the average value in the sequence, sorted in descending order.

integers_as_list = [int(num) for num in input().split()]

average = sum(integers_as_list) / len(integers_as_list)
above_average_list = [el for el in integers_as_list if el > average]
above_average_list.sort(reverse=True)
final_list = []
for i in range(5):
    if i < len(above_average_list):
        final_list.append(above_average_list[i])

if final_list:
    print(*final_list, sep=" ")
else:
    print('No')
