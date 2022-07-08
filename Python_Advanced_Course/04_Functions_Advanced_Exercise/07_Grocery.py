def grocery_store(**kwargs):
    result_dict = dict(sorted(kwargs.items(), key=lambda item: (-item[1], -len(item[0]), item[0])))

    result = []

    for k, v in result_dict.items():
        result.append(f'{k}: {v}')

    return '\n'.join(result)

# print(grocery_store(
#     bread=5,
#     pasta=12,
#     eggs=12,
# ))
# print(grocery_store(
#     bread=2,
#     pasta=2,
#     eggs=20,
#     carrot=1,
# ))
