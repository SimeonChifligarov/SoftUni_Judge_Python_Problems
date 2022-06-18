size_of_rhombus_as_int = int(input())


for i in range(size_of_rhombus_as_int):
    print(" " * (size_of_rhombus_as_int - i - 1), end="")
    print("* " * (i + 1))

for j in range(size_of_rhombus_as_int):
    print(" " * (j + 1), end="")
    print("* " * (size_of_rhombus_as_int - j - 1))
