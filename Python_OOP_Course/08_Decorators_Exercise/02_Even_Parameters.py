def even_parameters(func):
    ERROR_MESSAGE = 'Please use only even numbers!'

    def wrapper(*args):
        if not all(type(arg) == int for arg in args) or not all(arg % 2 == 0 for arg in args):
            return ERROR_MESSAGE

        return func(*args)

    return wrapper

# @even_parameters
# def add(a, b):
#     return a + b
#
#
# print(add(2, 4))
# print(add("Peter", 1))
#
#
# @even_parameters
# def multiply(*nums):
#     result = 1
#     for num in nums:
#         result *= num
#     return result
#
#
# print(multiply(2, 4, 6, 8))
# print(multiply(2, 4, 9, 8))
