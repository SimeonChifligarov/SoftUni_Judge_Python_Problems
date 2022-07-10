def flights(*args):
    list_of_data = list(args)

    data_as_dict = {}
    for i in range(0, len(list_of_data), 2):
        if list_of_data[i] == "Finish":
            break
        if list_of_data[i] not in data_as_dict:
            data_as_dict[list_of_data[i]] = 0
        data_as_dict[list_of_data[i]] += int(list_of_data[i + 1])

    return data_as_dict


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
