def get_products_of_all_ints_except_at_index(lst):
    """ 

    >>> get_products_of_all_ints_except_at_index([1, 7, 3, 4])
    [84, 12, 28, 21]

    """

    prods_before_index = [None] * len(lst)
    # For each integer, find the product of all the integers
    # before it, storing the total product so far each time

    # start index 0 at 1, b/c no ints before it
    prod_so_far = 1
    for i in xrange(len(lst)):
        prods_before_index[i] = prod_so_far
        prod_so_far *= lst[i]

# for this after index calc, let's mult. 
    prods_after_index = [None] * len(lst)
    prod_so_far = 1
    for i in xrange(len(lst) - 1, -1, -1):
        prods_after_index[i] = prod_so_far
        prod_so_far *= lst[i]

    products_except_at_index = [x * y for x, y in zip(prods_before_index,
                                prods_after_index)]
    
    return products_except_at_index

    #   after one pass, have [1, 1, 7, 21]


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n Yaaaahhooo all tests passed! \n"
