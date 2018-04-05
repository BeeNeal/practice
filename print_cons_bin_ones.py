# print consecutive ones appearing in a binary number


n = int(raw_input().strip())
def num_to_binary(n):
    """converts num to binary

    >>> num_to_binary(6)
    [0, 1, 1]


    """

    bin_digits = []

    if n == 0:
        print 0

    while n > 0:
        # n % 2 will be 0 or 1
        bin_digits.append(n % 2)
        n /= 2
        # would reverse, but don't need to for this problem
    return bin_digits


def consecutive_ones_from_binary_num(bin_digits):
    """takes in binary number in list form, returns num of consecutive ones

    >>> consecutive_ones_from_binary_num([0, 1, 1, 0])
    2

    >>> consecutive_ones_from_binary_num([0, 1, 1, 1, 1, 1])
    5

    """

    if len(bin_digits) < 1:
        return 0

    max_consecutive_ones = 0
    cons_ones = 0

    for i in range(len(bin_digits) - 1):
        if bin_digits[i] == 1:
            cons_ones += 1
            # print cons_ones
        else:  # this else is never being triggered because not ending with zero!
            if cons_ones > max_consecutive_ones:
                max_consecutive_ones = cons_ones
                cons_ones = 0
            else:
                cons_ones = 0
                
        if i == len(bin_digits) - 1:
            print max_consecutive_ones
            print "hello"

    print max_consecutive_ones

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n *** TEST'S PASSED! You're a kickass SWE!"
