def even_odd_filter(**kwargs):
    result_dict = {}

    for key in kwargs:
        if key == 'odd':
            result_dict[key] = [el for el in kwargs[key] if not el % 2 == 0]
        elif key == 'even':
            result_dict[key] = [el for el in kwargs[key] if el % 2 == 0]

    real_result_dict = dict(sorted(result_dict.items(), key=lambda item: -len(item[1])))

    return real_result_dict


# print(even_odd_filter(
#     odd=[1, 2, 3, 4, 10, 5],
#     even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
# ))
# 
# print(even_odd_filter(
#     odd=[2, 2, 30, 44, 10, 5],
# ))
