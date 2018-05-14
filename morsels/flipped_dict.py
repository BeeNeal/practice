
def flipped_dict(dict_of_lists):
    """

    >>> flipped_dict({'a':[1, 2], 'b':[2, 3], 'c': [2]})
    {1:['a'], 2:['b', 'c'], 3:['b']}

    """

    # want to iterate through the values of each key and assign each value as a 
    # key of new flipped dict. Assign current key as value in new list value
    flipped = dict()
    for key in dict_of_lists:
        lst_vals = dict_of_lists[key]
        for val in lst_vals:
            if val not in flipped:
                flipped[val] = list(key)
            else:
                flipped[val].append(key)

    return flipped

# O(n^2) runtime

print flipped_dict({'a':[1, 2], 'b':[2, 3], 'c': [2], 'd':[]})