def sorting_cheeses(**cheeses_dict):
    result_as_list = []

    cheeses_dict = sorted(
        cheeses_dict.items(),
        key=lambda x: (-len(x[1]), x[0]))

    for cheese_name, cheese_quantity_list in cheeses_dict:
        result_as_list.append(cheese_name)

        quantity_list = sorted(cheese_quantity_list, reverse=True)
        result_as_list.extend([str(el) for el in quantity_list])

    result = '\n'.join(result_as_list)
    return result

# print(
#     sorting_cheeses(
#         Parmesan=[102, 120, 135],
#         Camembert=[100, 100, 105, 500, 430],
#         Mozzarella=[50, 125],
#     )
# )
