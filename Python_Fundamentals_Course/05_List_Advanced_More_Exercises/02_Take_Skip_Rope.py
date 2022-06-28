# 3.	Take/Skip Rope from More Exercises: Lists Advanced

complete_message = [el for el in input()]

dig_from_complete_message = [int(el) for el in complete_message if el.isdigit()]

complete_message = [el for el in complete_message if not el.isdigit()]

take_list = [dig_from_complete_message[el_index] for el_index in range(len(dig_from_complete_message)) if
             el_index % 2 == 0]
skip_list = [dig_from_complete_message[el_index] for el_index in range(len(dig_from_complete_message)) if
             not el_index % 2 == 0]

final_message = []
for index in range(len(take_list)):
    for i in range(take_list[index]):
        if len(complete_message) > 0:
            final_message.append(complete_message[0])
            complete_message.pop(0)
    if complete_message:
        for j in range(skip_list[index]):
            complete_message.pop(0)

print(*final_message, sep="")
