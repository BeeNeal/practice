# Given a list, return bool if 2 numbers in the list equal to a given sum


def has_complements(lst, suma):
    """
    has_complements([1, 3, 4, 4], 8)
    True

    has_complements([1, 2, 3, 4])
    False

     """

    # iterate over list, store the complement to the sum

    seen = set()
    for num in lst:
        pair = suma - num
        if pair in seen:
            return True
        else:
            seen.add(pair)

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "You got it, keep going!"
