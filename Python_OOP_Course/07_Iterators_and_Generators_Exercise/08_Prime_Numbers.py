def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


# # Pythonic way
# def is_prime(num):
#     return num > 1 and all(num % i for i in range(2, num))


def get_primes(list_of_integers):
    primes = filter(lambda n: is_prime(n), list_of_integers)
    for pr in primes:
        yield pr

# print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
