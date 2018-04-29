def calculateScore(text, prefixString, suffixString):
    """
    >>> calculateScore('nothing', 'bruno', 'ingenious')

    """
    


def generate_prefix_substrings(string):
    """Generate all prefix substrings of a given string."""

    prefixes = []

    for i in range(1, len(string)):
        prefixes.append(string[:i])
    return prefixes

def generate_suffix_substrings(string):
    """Generate all suffix substrings of a given string."""

    suffixes = []

    for i in range(1, len(string)):
        suffixes.append(string[-i:])
    return suffixes

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n Tests passed - yahooo string masta!"