def type_check(arg_type):
    ERROR_MESSAGE = 'Bad Type'

    def decorator(func):
        def wrapper(arg):
            if not type(arg) == arg_type:
                return ERROR_MESSAGE

            return func(arg)

        return wrapper

    return decorator

# @type_check(int)
# def times2(num):
#     return num * 2
#
#
# print(times2(2))
# print(times2('Not A Number'))
#
#
# @type_check(str)
# def first_letter(word):
#     return word[0]
#
#
# print(first_letter('Hello World'))
# print(first_letter(['Not', 'A', 'String']))
