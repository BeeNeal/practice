# Reverse words in a sentence without split or join
"""
    >>> rev("The quick brown fox")
    fox brown quick The
"""

def rev(s):
    """takes in string, reverses words"""

    words = []
    index = 0

    for i in range(len(s)):
        if s[i] == ' ':
            words.append(s[index:i])
            index = i + 1
        if i + 1 == len(s):
            words.append(s[index:i + 1])

    words.reverse()
    for word in words:
        print word, 


if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. You're a software engineer!\n"