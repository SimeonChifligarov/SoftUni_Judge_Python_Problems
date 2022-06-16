def rectangle(length, width):
    WRONG_VALUES_MESSAGE = "Enter valid values!"

    if not (isinstance(length, int) and isinstance(width, int)):
        return WRONG_VALUES_MESSAGE

    def area():
        return length * width

    def perimeter():
        return (length + width) * 2

    result_as_list = [f'Rectangle area: {area()}', f'Rectangle perimeter: {perimeter()}']

    return '\n'.join(result_as_list)


# print(rectangle(2, 10))
# print(rectangle('2', 10))
