# // for a single sorted list, the median value is defined as follows
# //  - in the case where the list is odd in length, the median value is the middle element
# //  - in the case where the list is even in length, the median value is the mean of the middle two elements
# //  - if the list is empty, the median value is None


a = [1,3,3,6,7]
b = [2,5,8,8,9,9]
c = [2,3,4,5,6,7]
d = []

# // complete function `findMedianTwo`, which takes two sorted lists and finds the median value across both those lists

def findMedianTwo(listA, listB):
    
    lst = listA + listB
    lst.sort()
    if len(listA) % 2 == 0:
        median = (lst[len(lst)/2] + lst[len(lst)/2 - 1]) / 2.0
    else:
        median = lst[len(lst)/2]

    return median

print findMedianTwo(a, b) == 6
print findMedianTwo(b, c) == 5.5
print findMedianTwo(a, d) == 3
print findMedianTwo(b, c)