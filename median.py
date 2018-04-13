# // for a single sorted list, the median value is defined as follows
# //  - in the case where the list is odd in length, the median value is the middle element
# //  - in the case where the list is even in length, the median value is the mean of the middle two elements
# //  - if the list is empty, the median value is None


a = [1,3,3,6,7]
b = [2,5,8,8,9,9]
c = [2,3,4,5,6,7]
d = []

# // complete function `findMedianTwo`, which takes two sorted lists and finds the median value across both those lists

# Easy O(n) solution
def findMedianTwo(listA, listB):
    
    lst = listA + listB
    lst.sort()
    if len(lst) % 2 == 0:
        median = (lst[len(lst)/2] + lst[len(lst)/2 - 1]) / 2.0
    else:
        median = lst[len(lst)/2]

    return median


print findMedianTwo(a, b) == 6
print findMedianTwo(b, c) == 5.5
print findMedianTwo(a, d) == 3
print findMedianTwo(b, c)


def findMedianTwo_optimized(listA, listB):
    """Takes 2 sorted lists, finds median value in O(log n) runtime"""


    if len(sorted_list) % 2 == 0:
        median = (lst[len(sorted_list)/2] + sorted_list[len(sorted_list)/2 - 1]) / 2.0
    else:
        median = sorted_list[len(sorted_list)/2]

    return median



print findMedianTwo_optimized(a, b) == 6
print findMedianTwo_optimized(b, c) == 5.5
print findMedianTwo_optimized(a, d) == 3
print findMedianTwo_optimized(b, c)


# working on counting the index, so once arrive at median int, can quit, O(logn)
def merge_two_sorted_lists(listA, listB):
    """Implement merge portion of merge sort"""

    i = 0
    j = 0
    count = 0

    while i < len(listA) and j < len(listB):
            if listA[i] < listB[j]:
                i = i + 1
            else:
                j = j + 1
            count += 1

    while i < len(listA):
        i = i + 1
        count += 1

    while j < len(listB):
        j = j + 1
        count += 1


a = [1,3,3,6,7]
b = [2,5,8,8,9,9]
c = [2,3,4,5,6,7]
d = []

def median(listA, listB):
    i = 0
    j = 0
    count = 0

    combined_len = len(listA) + len(listB)
    if combined_len % 2 != 0:
        while i + j < combined_len / 2 + 1:
            if listA[i] <= listB[j]:
                median = listA[i]
                i = i + 1
                print median
            else:
                median = listB[j]
                j = j + 1
                print median
            count += 1
    return median
    # if i > j:
    #     return listA[i]
    # else:
    #     return listB[j]
    else:
        while i + j < combined_len / 2:
            if listA[i] <= listB[j]:
                median = listA[i]
                i = i + 1
            else:
                median = listB[j]
                j = j + 1
        if i == j:
            median = listA[i] + listB[j] / 2.0
        elif i > j:
            if i - 1 > j:
                median = listA[i] + listA[i - 1] / 2.0
            else:
                pass

i = 3
j = 1
[1, 2, 3]
[2 3 4]
[ 1 2 2 3 3 4]

    return median
