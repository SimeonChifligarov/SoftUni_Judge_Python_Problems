# You are at the zoo and the meerkats look strange. You will receive 3 strings: (tail, body, head). You have to re-arrange the elements in a list, so that the animal looks normal again: (head, body, tail)

tail = input()
body = input()
head = input()

elements = [tail, body, head]
elements[0], elements[2] = elements[2], elements[0]

print(elements)
