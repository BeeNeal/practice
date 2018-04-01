"""Given an NxM matrix, if a cell is zero, set entire row and column to zeroes.

A matrix without zeroes doesn't change:

    >>> zero_matrix([[1, 2 ,3], [4, 5, 6], [7, 8, 9]])
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

But if there's a zero, zero both that row and column:

    >>> zero_matrix([[1, 0, 3], [4, 5, 6], [7, 8, 9]])
    [[0, 0, 0], [4, 0, 6], [7, 0, 9]]

Make sure it works with non-square matrices:

    >>> zero_matrix([[1, 0, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    [[0, 0, 0, 0], [5, 0, 7, 8], [9, 0, 11, 12]]
"""


def zero_matrix(matrix):
    """Given an NxM matrix, for cells=0, set their row and column to zeroes."""

    zero_position = []
    row = []

    for position, item in list(enumerate(matrix)):
        for i in range(len(item) - 1):
            if item[i] == 0:
                zero_position.append(i)
                row.append(position)

    while zero_position:
        # converts whole row that contains 0 to 0
        row_pos = row.pop()
        matrix[row_pos] = [0] * len(matrix[row_pos])

        # then finds other rows' zeroes and converts them
        pos = zero_position.pop()
        for item in matrix:
            item[pos] = 0

    return matrix

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** TESTS PASSED! YOU'RE DOING GREAT!\n"
