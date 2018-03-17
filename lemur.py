"""Leaping lemur.

Calculate the fewest number of jumps the lemur needs to
jump to the last tree. The lemur can jump 1 or 2 branches.
It cannot use deadly branch (1 in the list).

    >>> lemur([0])
    0

    >>> lemur([0, 0])
    1

    >>> lemur([0, 0, 0])
    1

    >>> lemur([0, 1, 0])
    1

    >>> lemur([0, 0, 1, 0])
    2

    >>> lemur([0, 0, 0, 0, 1, 0, 0, 1, 0])
    5

    >>> lemur([0, 0, 1, 0, 1, 0, 0, 0, 0, 0])
    5

    >>> lemur([0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    7
"""

# first try hopping 2, if out of range, jumps + 1, return jumps


# def  lemur(branches):
#     """Return number of jumps needed."""

#     assert branches[0] == 0, "First branch must be alive"
#     assert branches[-1] == 0, "Last branch must be alive"

#     jumps = 0
#     current_branch = 0

#     if branches == [0]:
#         return jumps
#     while current_branch < len(branches):
#         try:
#             if branches[current_branch + 2] == 1:
#                 current_branch += 1
#             else:
#                 current_branch += 2
#             jumps += 1
#         except IndexError:
#             if current_branch + 2 == len(branches):
#                 jumps += 1
#                 break
#             else:
#                 break

#     return jumps

# alternative answer

def  lemur(branches):
    """Return number of jumps needed."""

    assert branches[0] == 0, "First branch must be alive"
    assert branches[-1] == 0, "Last branch must be alive"

    n_jumps = 0
    at = 0

    while at < len(branches) - 1:
        at += 2
        if at >= len(branches) or branches[at] == 1:
            at -= 1
        n_jumps += 1

    return n_jumps

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NICE JUMPING!\n"