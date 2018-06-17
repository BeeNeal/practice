def quick_sort(A):
    """Provide UI to call QS by entering in list of nums"""

    quick_sort2(A, 0, len(A) - 1)


def quick_sort2(A, low, high):
    """Recursively calls QS on both sides of pivot"""

    # Uses selection sort if # of items in lst less than 20
    if len(A) < 20 and low < high:
        print "using selection sort instead"
        quick_selection(A, low, high)

    elif low < high:  # if more than one num in list, do the QS
        p = partition(A, low, high)
        quick_sort2(A, low, p - 1)
        quick_sort2(A, p + 1, high)


def partition(A, low, high):
    """Performs the quick sort"""

    # get pivot index and pivot value
    pivot_index = get_pivot(A, low, high)
    pivot_value = A[pivot_index]

    # swap the pivot number and low position, border becomes low position
    A[pivot_index], A[low] = A[low], A[pivot_index]
    border = low

    for i in range(low, high + 1):
        if A[i] < pivot_value:
            border += 1
            A[i], A[border] = A[border], A[i]
        A[low], A[border] = A[border], A[low]

        return border


def get_pivot(A, low, high):
    """Returns index of the median of low, high, and mid positions."""

    mid = low + high / 2

    s = sorted([A[low], A[mid], A[high]])
    if s[1] == A[low]:
        return low
    elif s[1] == A[mid]:
        return mid
    else:
        return high

# if not allowed to use tim sort in sorting alg

# a = A[low]
# b = A[mid]
# c = A[high]
# if a > b:
#     if a < c:
#         pivot_i = a
#     elif b > c:
#         pivot_i = b
#     else:
#         pivot_i = c
# else:
#     if a > c:
#         pivot_i = a
#     elif b < c:
#         pivot_i = b
#     else:
#         pivot_i = c


def quick_selection(x, first, last):
    """O(n^2), useful for datasets less than 10,000"""

    # set our first loop, setting the min index as first item's index 
    # (b/c that's all we've seen so far)
    for i in range(first, last):
        minIndex = i
        # set second loop, go through list to find smallest num
        for j in range(i + 1, last + 1):
            if x[j] < x[minIndex]:
                minIndex = j
        # After the second loop, as long as we aren't swapping same thing in place,
        # swap index of smallest num with index of i (i will be the first item in 
        # the nonsorted part of the list)
        if minIndex != i:
            x[i], x[minIndex] = x[minIndex], x[i]
