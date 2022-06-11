from collections import deque

END_COMMAND = "End"
PAID_COMMAND = "Paid"

queue = deque()
while True:
    command = input()
    if command == END_COMMAND:
        print(f"{len(queue)} people remaining.")
        break

    if command == PAID_COMMAND:
        while len(queue):
            print(queue.popleft())
    else:
        current_name = command
        queue.append(current_name)
