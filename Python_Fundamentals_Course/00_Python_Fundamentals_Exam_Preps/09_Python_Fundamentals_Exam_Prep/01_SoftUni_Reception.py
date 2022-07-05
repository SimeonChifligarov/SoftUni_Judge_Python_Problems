# •	On first three lines -  each employee efficiency -  integer in range [1 - 100]
# •	On the fourth line - students count – integer in range [0 – 10000]
# •	Input will always be valid and in the range specified
import math

employee_1_efficiency = int(input())
employee_2_efficiency = int(input())
employee_3_efficiency = int(input())
students_count = int(input())

eff_per_hour = employee_1_efficiency + employee_2_efficiency + employee_3_efficiency
hours_work_needed = math.ceil(students_count / eff_per_hour)
hours_for_breaks = hours_work_needed // 3
if hours_work_needed % 3 == 0 and not hours_work_needed == 0:
    hours_for_breaks -= 1

print(f'Time needed: {hours_work_needed + hours_for_breaks}h.')
