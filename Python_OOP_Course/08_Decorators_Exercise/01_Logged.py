def logged(some_func):
    def wrapper(*args):
        result = []

        func_result = some_func(*args)
        result.append(f'you called {some_func.__name__}{args}')
        result.append(f'it returned {func_result}')
        return '\n'.join(result)

    return wrapper

# @logged
# def func(*args):
#     return 3 + len(args)
#
#
# print(func(4, 4, 4))
#
#
# @logged
# def sum_func(a, b):
#     return a + b
#
#
# print(sum_func(1, 4))
