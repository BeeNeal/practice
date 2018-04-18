def urlify(string):
    """
    Takes in string and replaces spaces with '%'

    >>> urlify('Mr John Smith')
    'Mr%20John%20Smith'

    >>> urlify('')
    ''

    """

    return string.replace(" ", "%20")


def is_permutation(string, string2):
    """
    Takes in 2 strings, checks to see if they are permutations of eachother

    >>> is_permutation('string', 'srtngi')
    True
    >>> is_permutation('yes', 'no')
    False

    """

    if len(string) != len(string2):
        return False
    if len(set(string) - set(string2)) != 0:
        return False

    return True


def is_palindrome_permutation(string, string2):
    """ """
    pass


def one_away(string, string2):
    """ """
    pass


def string_compression(string):
    """
    Take in string, return character, and number of that character

    >>> string_compression('aaabbbbbddccc')
    'a3b5d2c3'
    >>> string_compression('abc')
    'abc'
    >>> string_compression('')
    ''
    >>> string_compression('abcca')
    'abc2a'
    >>> string_compression('1122311')
    '1222312'

    """
    char_count = 1
    compressed = ''

    if len(string) == 0:
        return ''

    for i in range(1, len(string)):
        if string[i - 1] == string[i]:
            char_count += 1
        else:
            compressed += string[i - 1]
            if char_count > 1:
                compressed += str(char_count)
            char_count = 1
    compressed += string[i]
    if char_count > 1:
        compressed += str(char_count)
    return compressed


def rotate_matrix(matrix):
    """ """
    pass


def zero_matrix():
    """ """
    pass


def string_rotation(string, string2):
    """ """
    pass


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n Tests passed - yahooo string masta!"
