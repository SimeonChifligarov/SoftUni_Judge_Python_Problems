def concatenate(*args, **kwargs):
    result = []
    for string in args:
        result.append(string)

    result_string = ''.join(result)

    for key, value in kwargs.items():
        if key in result_string:
            result_string = result_string.replace(key, value)

    return result_string

# print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
# print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
