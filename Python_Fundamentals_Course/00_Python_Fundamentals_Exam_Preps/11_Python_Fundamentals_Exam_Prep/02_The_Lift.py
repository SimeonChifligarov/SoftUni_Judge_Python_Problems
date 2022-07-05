# •	On the first line you, will receive how many people are waiting to get on the lift
# •	On the second line, you will you will receive the current state of the lift separated by " ".

waiting_people = int(input())
current_people = waiting_people

current_state = [int(wagon) for wagon in input().split()]

all_seats = len(current_state) * 4
available_seats = all_seats - sum(current_state)

new_state = current_state.copy()

for wagon in range(len(current_state)):
    while new_state[wagon] < 4 and current_people > 0:
        new_state[wagon] += 1
        current_people -= 1
        available_seats -= 1

if current_people == 0 and available_seats > 0:
    print('The lift has empty spots!')
elif current_people > 0:
    print(f'There isn\'t enough space! {current_people} people in a queue!')

print(*new_state, sep=" ")
