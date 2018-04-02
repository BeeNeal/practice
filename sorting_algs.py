"""  
    >>> bubble_sort([3, 7, 4, 1, 2, 6, 9])
    [1, 2, 3, 4, 6, 7, 9]

    >>> bubble_sort([9, 7, 8, 1, 6, 2, 6, 3])
    [1, 2, 3, 6, 6, 7, 8, 9]

    >>> bubble_sort([])
    []

"""

def bubble_sort(lst):
    """Takes in list, uses bubble sort to return sorted list."""

    for i in range(len(lst) - 1):
        # keep track of if swap, so can win quicker
        made_swap = False

        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                made_swap = True
        if not made_swap:
                # if no swaps need to be made, we're done!
                break
    return lst


def selection_sort(lst):
    """Takes in list, uses selection sort to return sorted list."""

    for i in range(len(lst) - 1, 0, -1):
        pos_of_max = 0

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** TESTS PASSED! Sort master!\n"


# problems solved: carefully watch your indentation

# O(n^2) is the best we can do for bubble sort
