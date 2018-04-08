# Reverse words in a sentence without split or join
"""
    >>> rev("The quick brown fox")
    fox brown quick The

    >>> find_mode([1, 2, 2, 3, 3, 4])
    [2, 3]
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


# find mode of list of numbers

def find_mode(lst):
    """takes in list of ints, returns mode"""

    num_counts = {}

    for num in lst:
        num_counts[num] = num_counts.get(num, 0) + 1

    v = sorted(num_counts.values())
    v.reverse()
    mode_count = v[0]

    mode = []

    for num in num_counts:
        if num_counts[num] == mode_count:
            mode.append(num)
    return mode

if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. Nice job!\n"