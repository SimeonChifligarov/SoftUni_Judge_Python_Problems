def age_assignment(*args, **kwargs):
    result_dict = {}
    result = []

    for name in args:
        result_dict[name] = kwargs[name[0]]

    for k, v in sorted(result_dict.items(), key=lambda item: item[0]):
        result.append(f'{k} is {v} years old.')

    return '\n'.join(result)


# print(age_assignment("Peter", "George", G=26, P=19))
# print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
