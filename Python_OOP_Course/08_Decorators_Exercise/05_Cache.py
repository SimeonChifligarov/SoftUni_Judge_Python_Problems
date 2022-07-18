def cache(func):
    log = {}

    def wrapper(num):
        for current_num in range(num + 1):
            if num not in log:
                log[num] = func(num)
        # if num not in log:
        #     log[num] = func(num)

        return log[num]

    wrapper.log = log

    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

#
# print(fibonacci(3))
# print(fibonacci.log)
#
# fibonacci(4)
# print(fibonacci.log)
