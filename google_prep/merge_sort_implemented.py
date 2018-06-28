def merge_sort(A):
    """UI for the merge sort"""
    merge_sort2(A, 0, len(A) - 1)

def merge_sort(A, first, last): # take in list and first/last indices
    """separating the lists into 1 elem """

    if first < last:  # if otherwise, would be an empty list
        middle = (first + last)//2
        merge_sort2(A, first, middle)
        merge_sort2(A, middle+1, last)
        merge(A, first, middle, last)

def merge(A, first, middle, last):
    """ """

    L = A[first:middle + 1]
    R = A[middle+ 1: last+1]
    #  tack on large number so know when reach end
    L.append(float('inf'))
    R.append(float('inf'))
    i = j = 0 # i for L, j for R

    # meat of the merge: if the L if smaller than R, append, otherwise append R
    for k in range(first, last + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1