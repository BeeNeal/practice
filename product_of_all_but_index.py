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

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n Yaaaahhooo all tests passed! \n"
