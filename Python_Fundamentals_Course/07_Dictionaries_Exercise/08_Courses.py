course_student = input()

courses_dict = {}

while not course_student == "end":
    c_s_split = course_student.split(" : ")
    course = c_s_split[0]
    student = c_s_split[1]
    if course not in courses_dict:
        courses_dict[course] = []
    courses_dict[course].append(student)
    course_student = input()

# sorted_courses = sorted(courses_dict.items(), key=lambda x: -len(x[1]))
#
# for course, students in sorted_courses:
#     print(f"{course}: {len(students)}")
#     for stud in sorted(students):
#         print(f"-- {stud}")


for course, students in courses_dict.items():
    print(f"{course}: {len(students)}")
    for stud in students:
        print(f"-- {stud}")
