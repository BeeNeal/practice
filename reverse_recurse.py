"""Reverse a string using recursion.

For example::

    >>> rev_string("")
    ''

    >>> rev_string("a")
    'a'

    >>> rev_string("porcupine")
    'enipucrop'

"""


def rev_string(s):
    """Return reverse of string using recursion.

    You may NOT use the reversed() function!
    """
    # can put new_string as default funct, but then it doesn't reset the var once
    # the function is done. Leaky.
    # new_string = ''

    # if astring == '':
    #     return ''

    # elif astring is not None:
    #     new_string += astring[-1]
    #     rev_string(astring[:-1])
    #     return new_string

    # # return ''.join(new_string)
    # return new_string
# Problem - initializing list/string overwrites it each time instead of adds to, 
# so I end up with only the last element, not all of them

    if len(s) < 2:
        return s

    return s[-1] + rev_string(s[:-1])

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. !KROW DOOG\n"

        # new_string = rev_string(new_string[-2::-1])
