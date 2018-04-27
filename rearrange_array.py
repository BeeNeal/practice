# You are given a list of integers. Write a function that returns a list with 
# original values ordered by largest int, smallest int, second largest int, 
# second smallest int, third largest int, and so on.  You may modify the input
 # list in place and return it or you may create and return a new list.

def arrange_array(arr):
    """
    >>> arrange_array([2, 5, -12, 24, 0, -1])
    [24, -12, 5, -1, 2, 0]

    >>> arrange_array([2, 5, -12, 24, 0, -1, 6])
    [24, -12, 6, -1, 5, 0, 2]

    >>> arrange_array([])
    []

    """
    l = len(arr)
    arr.sort()
    asc = arr
    desc = list(reversed(asc))
    
    arranged_ints = []
    for i in range(check_length(l)):
        arranged_ints.append(asc.pop())
        arranged_ints.append(desc.pop())
    if l % 2 != 0:
        return arranged_ints[:-1]

    return arranged_ints


def check_length(l):

    # if length of arr is odd, need range to increase by one, otherwise can
    # use range length of arr

    if l % 2 != 0:
        range_val = (l + 1) / 2
    else:
        range_val = l/2
    return range_val


# could probably solve this with better runtime with a modified merge sort

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "Yahhhoo! Tests passed"

# have nums in correct order, can we just merge them?