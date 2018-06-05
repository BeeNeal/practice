#  all recursive algorithms must obey three important laws:

# A recursive algorithm must have a base case.
# A recursive algorithm must change its state and move toward the base case.
# A recursive algorithm must call itself, recursively.

def sum_list_recursively(num_list):
    """Sum numbers in a list using recursion 
    >>> print sum_list_recursively([1, 3, 5, 7, 9])
    25

    """

    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + sum_list_recursively(num_list[1:])


# takeaways: remember the len list 1 base case w/ passing in rest of list model


def factorial(n):
    """Return the factorial of a non-negative integer using recursion.

    >>> factorial(6)
    720
    """

    # base case
    if n <= 1:
        return 1

    else:
        return n * factorial(n - 1)

# def factorial(n):
#     """return factorial of n not using recursion"""

#     num = 1
#     for i in range(1, n+1):
#         num *= i
#     return num


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "recursion master!"