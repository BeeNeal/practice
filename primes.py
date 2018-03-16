def primes(count):
    """Takes in int, returns list of that many primes"""

    primes = []
    num = 2
    while count > 0:
        if is_prime(num):
            primes.append(num)
            count -= 1
            num += 1
        else:
            num += 1

    return primes


def is_prime(num):
    """Takes in integer and returns boolean for if num is prime"""
    if num == 2:
        return True

    if num % 2 == 0:
        return False

    if num < 2:
        return False

    n = 3

    while n * n <= num:
        if num % n == 0:
            return False
            n += 2
        else:
            n += 2

    return True
