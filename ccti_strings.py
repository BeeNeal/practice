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
    """Take in string, return character, and number of that character
    >>> string_compression('aaabbbbbddccc')
    'a3b5d2c3'
    >>> string_compression('abc')
    'abc'
    >>> string_compression('')
    ''
    >>> string_compression('1122311')
    '1222312'

    """
    # takes care of already compressed strings and empty strings
    if len(string) == len(set(string)):
        return string

    index = 0
    compressed_string = ''
    for i in range(len(string)):
        # when hit end of the string, won't hit a dif char, so manually slice at end
        if all(c == string[-1] for c in string[index:]):
            char = string[index:]
            compressed_string += string[-1] + str(len(char))
            break
        elif string[i] != string[index]:
            char = string[index:i]
            # here see if we can do inplace - always know the compressed string 
            #will be 2 char more if compression
            compressed_string += string[i - 1] + str(len(char))
            index = i
    return compressed_string


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
