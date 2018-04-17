def urlify(string):
    """
    Takes in string and replaces spaces with '%'

    >>> urlify('Mr John Smith')
    'Mr%20John%20Smith'

    """

    return string.replace(" ", "%20")

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n yahooo string masta!"
