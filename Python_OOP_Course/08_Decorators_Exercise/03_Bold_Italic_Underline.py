def make_bold(func):
    def wrapper(*args, **kwargs):
        # result = []
        #
        # func_result = func(*args, **kwargs)
        # result.append('<b>')
        # result.append(func_result)
        # result.append('</b>')
        # return ''.join(result)

        func_result = func(*args, **kwargs)
        return f'<b>{func_result}</b>'

    return wrapper


def make_italic(func):
    def wrapper(*args, **kwargs):
        # result = []
        #
        # func_result = func(*args, **kwargs)
        # result.append('<i>')
        # result.append(func_result)
        # result.append('</i>')
        # return ''.join(result)

        func_result = func(*args, **kwargs)
        return f'<i>{func_result}</i>'

    return wrapper


def make_underline(func):
    def wrapper(*args, **kwargs):
        # result = []
        #
        # func_result = func(*args, **kwargs)
        # result.append('<u>')
        # result.append(func_result)
        # result.append('</u>')
        # return ''.join(result)

        func_result = func(*args, **kwargs)
        return f'<u>{func_result}</u>'

    return wrapper

# @make_bold
# @make_italic
# @make_underline
# def greet(name):
#     return f"Hello, {name}"
#
#
# print(greet("Peter"))
#
#
# @make_bold
# @make_italic
# @make_underline
# def greet_all(*args):
#     return f"Hello, {', '.join(args)}"
#
#
# print(greet_all("Peter", "George"))
