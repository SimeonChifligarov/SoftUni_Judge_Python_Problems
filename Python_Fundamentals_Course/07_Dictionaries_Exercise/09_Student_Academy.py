# You will receive n pair of rows. First you will receive the student's name,
# after that you will receive his grade. Check if the student already exists and if not, add him.
# Keep track of all grades for each student.

pair_of_rows = int(input())
students_grades_dict = {}

for _ in range(pair_of_rows):
    student = input()
    grade = float(input())
    if student not in students_grades_dict:
        students_grades_dict[student] = []
    students_grades_dict[student].append(grade)

# When you finish reading the data, keep the students with average grade higher than or equal to 4.50.
# Order the filtered students by average grade in descending order.

keeped_students = {}
#
# for stud, grades in students_grades_dict.items():
#     average_grade = sum(grades) / len(grades)
#     if average_grade >= 4.50:
#         keeped_students[stud] = average_grade
#
# sorted_keeped_students = sorted(keeped_students.items(), key=lambda x: -x[1])
# for keep_stud, grade in sorted_keeped_students:
#     print(f"{keep_stud} -> {grade :.2f}")


for stud, grades in students_grades_dict.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        keeped_students[stud] = average_grade

for keep_stud, grade in keeped_students.items():
    print(f"{keep_stud} -> {grade :.2f}")
