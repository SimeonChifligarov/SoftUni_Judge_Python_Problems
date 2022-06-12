number_of_students = int(input())

students_grades_as_dict = {}

for _ in range(number_of_students):
    student, grade = input().split()
    grade = float(grade)
    if student not in students_grades_as_dict:
        students_grades_as_dict[student] = []
    students_grades_as_dict[student].append(grade)

for student, grades in students_grades_as_dict.items():
    print(f"{student} -> {' '.join([f'{grade:.2f}' for grade in grades])} (avg: {sum(grades) / len(grades):.2f})")
