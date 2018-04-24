def calculateScore(text, prefixString, suffixString):
    """
    >>> calculateScore('nothing', 'bruno', 'ingenious')

    """
    pass

def calculate_prefix_score(string1, string2):
    """
    >>> calculate_prefix_score('nothing', 'bruno')
    2

    """

    prefix = ''
    prefix_start = string1[0]
    start_pre_match = string2.find(prefix_start)
    if start_pre_match != -1:
        prefix = string2[start_pre_match:]

    # add check for making sure the 'fixes' match
    return len(prefix)

def calculate_suffix_score(string1, string2):
    """
    >>> calculate_suffix_score('nothing', 'ingenious')
    3

    """

    suffix = ''
    suffix_start = string1[0]
    start_pre_match = string2.find(prefix_start)
    if start_pre_match != -1:
        prefix = string2[start_pre_match:]

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n Tests passed - yahooo string masta!"