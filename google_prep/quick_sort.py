
# provide user interface function, where they can pass in a list for sorting
def quick_sort(A):
    """Calls recursive QS function, takes in starting and ending indices"""

    quick_sort2(A, 0, len(A) - 1)

def quick_sort2(A, low, high):
    """ """

    if low < high:
        p = partition(A, low, high)
        # call recursive QS on all nums left of pivot
        quick_sort2(A, low, p - 1)
        # call recursive QS on all nums left of pivot
        quick_sort2(A, p + 1, high)


def partition(A, low, high):
    """Performs the quick sort"""

    pivot_index = get_pivot(A, low, high)
    pivot_value = A[pivot_index]
    A[pivot_index], A[low] = A[low], A[pivot_index]
    border = low

    for i in range(low, high + 1):
        if A[i] < pivot_value:
            border += 1
            A[i], A[border] = A[border], A[i]
        A[low], A[border] = A[border], A[low]


def get_pivot(A, low, high):
    """Returns median of low, high, and mid position.""" 

    mid = (low + high) // 2
    pivot = high
    if A[low] > A[high]:
        pivot = mid
    elif A[low] < A[high]:
        pivot = low
    return pivot
