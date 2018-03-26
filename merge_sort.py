def merge_sort(alist):
    """ """

    if len(alist) > 1:
        mid = len(alist) // 2
        l_half = alist[:mid]
        r_half = alist[mid:]

        merge_sort(l_half)
        merge_sort(r_half)

    i = 0  # keeps track of l_half index
    j = 0  # keeps track of r_half index
    k = 0  # keeps track of sorted_list index
    sorted_list = []
    while i < len(l_half) and j < len(r_half):
        if l_half[i] < r_half[j]:
            sorted_list[k] = l_half[i]
            i += 1
        else:
            sorted_list[k] = r_half[j]
            j += 1
        k += 1

    while i < len(l_half):
        sorted_list[k] = l_half[i]
        i += 1
        k += 1

    while j < len(r_half):
        sorted_list[k] = r_half[j]
        i += 1
        k += 1

alist = [50, 22, 89, 17, 76, 33, 44, 55, 21]
merge_sort(alist)
