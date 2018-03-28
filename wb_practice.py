def word_score(phrase):
    """Take in phrase of words, return word of highest score

    >>> print word_score('abc zab i')
    zab
    >>> print word_score('abc abbaa za')
    za

    """

    high_score = 0
    high_word = ''
    current = 0

    index = 0
    for i in range(len(phrase)):
        if phrase[i] != ' ' and i != len(phrase):
            current += ord(phrase[i]) - 96
        elif phrase[i] == ' ':
            if current > high_score:
                high_word = phrase[index: i]
                high_score = current
            index = i + 1
            current = 0
        elif i == len(phrase):
            print i, current, high_word
            current += ord(phrase[i]) - 96
            if current > high_score:
                high_word = phrase[index: i + 1]
                high_score = current
            index = i + 1
            current = 0

    return high_word


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. You're a kickass SWE!\n"
