"""  
    >>> bubble_sort([3, 7, 4, 1, 2, 6, 9])
    [1, 2, 3, 4, 6, 7, 9]

    >>> bubble_sort([9, 7, 8, 1, 6, 2, 6, 3])
    [1, 2, 3, 6, 6, 7, 8, 9]

    >>> bubble_sort([])
    []

    >>> selection_sort([])
    []

    >>> selection_sort([9, 7, 8, 1, 6, 2, 6, 3])
    [1, 2, 3, 6, 6, 7, 8, 9]

"""

def bubble_sort(lst):
    """Takes in list, uses bubble sort to return sorted list."""

    for i in range(len(lst) - 1):
        # keep track of if swap, so can win quicker
        made_swap = False
        # range is len(lst) - 1 - i, because we already know the last elements
        # that have been touched will be sorted
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                made_swap = True

        # if no swaps need to be made, we're done!
        if not made_swap:
            break
    return lst


def selection_sort(lst):

    # want to stop loop at 2nd to last, as nested loop will handle the last val
    for i in range(0, len(lst) - 1):
        # by setting our min_index as our next index, we keep the sorted part of 
        # the list properly sorted, and don't touch it again
        min_index = i
        # start this loop as one more than i, go to the end of the list
        for j in range(i + 1, len(lst)):
            # loop through list, finding the index of the smallest number
            if lst[j] < lst[min_index]:
                min_index = j
        # swap the smallest val with current index,so next smallest int of list
        # is in proper place
        if min_index != i:
            lst[i], lst[min_index] = lst[min_index], lst[i]

    return lst


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** TESTS PASSED! Sort master!\n"


# problems solved: carefully watch your indentation on these nested loops

# The trick to bubble sort is adjusting the range accordingly to len(lst) - 1 -i
# for the nested j index loop, and that all the actual swapping happens in the j
# loop.

# O(n^2) is the best we can do for bubble sort and selection sort

# another way to do selection sort would be to use max_index, and get highest val
# and put at end of list. Doesn't affect performance though.
