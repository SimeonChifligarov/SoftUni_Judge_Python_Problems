initial_schedule = input().split(', ')

while True:
    command = input()

    if command == 'course start':
        break

    tokens = command.split(':')
    real_command = tokens[0]

    if real_command == 'Add':
        lesson_title = tokens[1]
        if lesson_title not in initial_schedule:
            initial_schedule.append(lesson_title)

    elif real_command == 'Insert':
        lesson_title, index = tokens[1], int(tokens[2])
        if lesson_title not in initial_schedule:
            initial_schedule = initial_schedule[:index] + [lesson_title] + initial_schedule[index:]
    elif real_command == 'Remove':
        lesson_title = tokens[1]
        if lesson_title in initial_schedule:
            initial_schedule.remove(lesson_title)
    elif real_command == 'Swap':
        lesson_title, swap_title = tokens[1], tokens[2]
        lesson_exercise = f'{lesson_title}-Exercise'
        swap_exercise = f'{swap_title}-Exercise'
        if lesson_title in initial_schedule and swap_title in initial_schedule:
            index_one = initial_schedule.index(lesson_title)
            index_two = initial_schedule.index(swap_title)
            initial_schedule[index_one], initial_schedule[index_two] = initial_schedule[index_two], initial_schedule[
                index_one]
        if lesson_exercise in initial_schedule:
            # index_one_exercise = initial_schedule.index(lesson_exercise)
            initial_schedule.remove(lesson_exercise)
            initial_schedule = initial_schedule[:index_two + 1] + [lesson_exercise] + initial_schedule[index_two + 1:]
        if swap_exercise in initial_schedule:
            # index_swap_exercise = initial_schedule.index(swap_exercise)
            initial_schedule.remove(swap_exercise)
            initial_schedule = initial_schedule[:index_one + 1] + [swap_exercise] + initial_schedule[index_one + 1:]

    elif real_command == 'Exercise':
        lesson_title = tokens[1]
        lesson_exercise = f'{lesson_title}-Exercise'
        if lesson_title in initial_schedule and lesson_exercise not in initial_schedule:
            index_one = initial_schedule.index(lesson_title)
            initial_schedule = initial_schedule[:index_one + 1] + [lesson_exercise] + initial_schedule[index_one + 1:]
        if lesson_title not in initial_schedule:
            initial_schedule.append(lesson_title)
            initial_schedule.append(lesson_exercise)

for i in range(len(initial_schedule)):
    print(f'{i + 1}.{initial_schedule[i]}')
