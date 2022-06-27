# Write a program that, depending on the first line of the input, reads an int, double or string.
# •	If the data type is int, multiply the number by 2.
# •	If the data type is real, multiply the number by 1.5 and format it to the second decimal point.
# •	If the data type is string, surround the input with "$".

data_type = input()
data_value = input()

if data_type == "int":
    print(f'{int(data_value) * 2}')
elif data_type == "real":
    print(f'{float(data_value) * 1.5 :.2f}')
elif data_type == "string":
    print(f'${data_value}$')
