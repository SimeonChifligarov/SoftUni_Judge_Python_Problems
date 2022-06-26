# You will receive a single number n. On the next n lines you will receive names of courses.
# You have to create a list of them and print it

number = int(input())
list_of_courses = []

for n in range(1, number + 1):
    current_course = input()
    list_of_courses.append(current_course)

print(list_of_courses)
