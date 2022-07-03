box_of_clothes = [int(el) for el in input().split()]

capacity_of_a_rack = int(input())

number_of_racks = 1
current_sum_of_clothes = 0

for _ in range(len(box_of_clothes)):
    current_cloth = box_of_clothes.pop()
    current_sum_of_clothes += current_cloth
    if current_sum_of_clothes > capacity_of_a_rack:
        number_of_racks += 1
        current_sum_of_clothes = current_cloth

print(number_of_racks)
