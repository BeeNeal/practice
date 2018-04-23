
# remove duplicate from string
def remove_duplicates(string):
    """
    >>> remove_duplicates('bananas')
    'bans'
    """

    present_chars = set()
    duplicates_removed = ''

    for char in string:
        if char in present_chars:
            continue
        else:
            duplicates_removed += char
            present_chars.add(char)

    return duplicates_removed


# reverse a string using iteration and recursion
def rev_string_recursively(string):
    """
    >>> rev_string_recursively('string')
    'gnirts'

    >>> rev_string_recursively('')
    ''

    """
    if len(string) < 2:
        return string

    return string[-1] + rev_string_recursively(string[:-1])


def rev_string_iteratively(string):
    """
    >>> rev_string_iteratively('string')
    'gnirts'

    >>> rev_string_iteratively('')
    ''

    """
    rev_string = ''
    for i in range(1, len(string) + 1):
        rev_string += string[-i]

    return rev_string



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "NICE! Tests passed"
