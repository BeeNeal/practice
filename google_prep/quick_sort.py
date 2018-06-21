
# provide user interface function, where they can pass in a list for sorting
def quick_sort(A):
    """Calls recursive QS function, sets initial high/low indices"""

    quick_sort2(A, 0, len(A) - 1)


def quick_sort2(A, low, high):
    """Recursively calls QS on both sides of pivot"""

    # can improve performance by setting an item threshold, and if less than
    # the threshold, use selection sort


    if low < high:  # if more than one item in list to be sorted, call partition
        p = partition(A, low, high)
        # call recursive QS on all nums left of pivot
        quick_sort2(A, low, p - 1)
        # call recursive QS on all nums right of pivot
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
            border += 1  # each time swap a num to the left, move border 1 to right
            A[i], A[border] = A[border], A[i]
        # Once has gone through whole list, switch border with pivot value
        # (which is in low position)
        A[low], A[border] = A[border], A[low] 

    return 


def get_pivot(A, low, high):
    """Returns index of the median of low, high, and mid positions.""" 

    mid = (low + high) / 2   # would use floor div '//' if in py3
    pivot_index = high
    if A[low] > A[high]:
        pivot_index = mid
    elif A[low] < A[high]:
        pivot_index = low
    return pivot_index
