# Given an array of integers, find the highest product you can get from three of 
# the integers.

def highest_product(int_lst):
    """
    Takes in list of 3 nums, return highest possible product

    >>> highest_product([1, 2, 3, 8, 6])
    144
    >>> highest_product([1, 2, 3, 8, -6, -4])
    192
    >>> highest_product([1, 2, 3, 8, -6, -2, -1])
    96
    >>> highest_product([-1, -8, -6, -2])
    -12
    >>> highest_product([0, -1, -8, -6, -2])
    0
    >>> highest_product([0, 1, -8, -6, -2])
    48
    >>> highest_product([-99, 88, 1, 2, 4])
    704
    >>> highest_product([4, 2, 1, 88, -99])
    704

    """

    # We're going to start at the 3rd item (at index 2)
    # so pre-populate highests and lowests based on the first 2 items.
    # We could also start these as None and check below if they're set
    # but this is arguably cleaner, better to initialize as data than none
    high = max(int_lst[0], int_lst[1])
    low = min(int_lst[0], int_lst[1])
    high_of_2 = int_lst[0] * int_lst[1]
    low_of_2 = int_lst[0] * int_lst[1]

    # Except this one--we pre-populate it for the first *3* items.
    # This means in our first pass it'll check against itself, which is fine.
    high_of_3 = int_lst[0] * int_lst[1] * int_lst[2]
    # Walk through items, starting at index 2

    for i in xrange(2, len(int_lst)):
        current = int_lst[i]
        # Do we have a new highest product of 3?
        # It's either the current highest,
        # or the current times the highest product of two
        # or the current times the lowest product of two
        high_of_3 = max(high_of_3, current * high_of_2, current * low_of_2)

        # Do we have a new highest product of two?
        high_of_2 = max(high_of_2, current * high, current * low)

        # Do we have a new lowest product of two?
        low_of_2 = min(low_of_2, current * high, current * low)
    
        # Do we have a new highest?
        high = max(high, current)
        # Do we have a new lowest?
        low = min(low, current)

    return high_of_3

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
            print "\n*** ALL TESTS PASSED. Yahoo!\n"