"""Count items in a list recursively.

For example:

        >>> count_recursively([])
        0

        >>> count_recursively([1, 2, 3])
        3

        >>> count_recursively([1, 2, 3, 5, 6])
        5

Print items in the list, using recursion.

For example::

   >>> print_recursively([1, 2, 3])
   1
   2
   3

   >>> print_recursively([1, 2, 3, 4])
   1
   2
   3
   4

Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.

For example:

    >>> recursive_index(5, [1, 3, 5, 2, 4])
    2

    >>> recursive_index("hey", ["hey", "there", "you"])
    0

    >>> recursive_index("you", ["hey", "there", "you"])
    2

    >>> recursive_index("zork", ["foo", "bar", "baz"]) is None
    True

"""


def recursive_index(needle, haystack):
    """Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.
    """

def print_recursively(lst):
    """Print items in the list, using recursion."""

    if not lst:
        return
    print lst[0]
    print_recursively(lst[1:])


def count_recursively(lst):
    """Return number of items in a list, using recursion."""

    count = 0
    # base case
    if not lst:
        return 0
    count = count_recursively(lst[1:]) + 1
    return count


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GO YOU!\n"
