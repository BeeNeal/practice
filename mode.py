"""Find the most frequent num(s) in nums.

Return the set of nums that are the mode::

    >>> find_mode([1]) == set([1])
    True

    >>> find_mode([1, 2, 2, 2]) == set([2])
    True

If there is a tie, return all::

    >>> find_mode([1, 1, 2, 2]) == set([1, 2])
    True

    >>> find_mode([1, 1, 2, 2])
    set([1, 2])
"""


def find_mode(nums):
    """Find the most frequent num(s) in nums."""

    mode = set()
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    highest_count = sorted(counts.values())[0]

# want to find the highest count, can do that by sorting counts.values(), then
# iterate through keys and any with that value get added to mode set

    for count in counts:
        if counts[count] == highest_count:
            mode.add(count)

    return mode

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. HOORAY!\n"
