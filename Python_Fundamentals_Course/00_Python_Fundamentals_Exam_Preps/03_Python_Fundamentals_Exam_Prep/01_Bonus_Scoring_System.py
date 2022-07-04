# •	On the first line you are going to receive the count of the students – an integer number in the range [0…50]
# •	On the second line you are going to receive the count of the lectures – an integer number in the range [0...50].
# •	On the third line you are going to receive the initial bonus – an integer number in the range [0….100].
# •	On the next lines, you will be receiving the attendances of each student.
# •	There will never be students with equal bonuses.
import math

students_count = int(input())
lectures_count = int(input())
initial_bonus = int(input())

max_bonus_points = 0
student_attendances = 0

for i in range(1, students_count + 1):
    current_attendance = int(input())
    total_bonus = current_attendance / lectures_count * (5 + initial_bonus)
    if total_bonus >= max_bonus_points:
        max_bonus_points = total_bonus
        student_attendances = current_attendance

print(f'Max Bonus: {math.ceil(max_bonus_points)}.')
print(f'The student has attended {math.ceil(student_attendances)} lectures.')
