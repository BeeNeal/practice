def sum_list_recursively(num_list):
    """Sum numbers in a list using recursion """

    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + sum_list_recursively(num_list[1:])

print(sum_list_recursively([1, 3, 5, 7, 9]))

# takeaways: remember the len list 1 base case w/ passing in rest of list model


def factorial(n):
    """Return the factorial of a non-negative integer."""

    # base case
    if n == 1:
        return 1
    else:
        pass