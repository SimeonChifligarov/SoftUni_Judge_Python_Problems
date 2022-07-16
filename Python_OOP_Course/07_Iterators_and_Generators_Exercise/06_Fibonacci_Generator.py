def fibonacci():
    fib_1 = 0
    fib_2 = 1
    yield fib_1
    yield fib_2
    fib_n_1 = fib_2  # fib previous number, i.e. number minus 1
    fib_n_2 = fib_1
    while True:
        fib_n = fib_n_2 + fib_n_1
        yield fib_n
        fib_n_2 = fib_n_1
        fib_n_1 = fib_n

# generator = fibonacci()
# for i in range(5):
#     print(next(generator))
