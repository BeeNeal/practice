# def array_sum(lst):

    # for i in xrange(len(lst)):
    #     if sum(lst[:i]) == sum(lst[i+1:]):
    #         return "YES"
    #     else:
    #         # print sum(lst[:i]), sum(lst[i+1:])
    #         continue
    # return "NO"

# above solution times out on HR

# better solution:

def equal_sums_on_sides_of_index(lst):

    total = sum(lst)
    left_side = 0

    for i in xrange(len(lst)):
        current = lst[i]
        total -= current
        if left_side == total:
            return "YES"
        left_side += current
    return "NO"

# O(n) runtime
