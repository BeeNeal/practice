# Using Python, write a function that finds all anagrams in a list of words and 
# prints a list of only those words. The output words can be in any order.  
# What is the big-O running time of your solution?

#    Sample input:  ['cat', 'eat', 'dare', 'bash', 'tea', 'dear', 'read']
#    Sample output: ['eat', 'dare', 'tea', 'dear', 'read']

import itertools

def return_all_anagrams(lst):
    """
    >>> sorted(return_all_anagrams(['cat', 'eat', 'dare', 'bash', 'tea', 'dear', 'read']))
    ['dare', 'dear', 'eat', 'read', 'tea']

    """
    all_anagrams = set()
    # word_set = [set(word) for word in lst]
    for a, b in itertools.combinations(lst, 2):
        if len(set(a) - set(b)) == 0:
            all_anagrams.add(a)
            all_anagrams.add(b)
    return list(all_anagrams)



def return_all_anagrams_2(lst):
    """
    >>> sorted(return_all_anagrams_2(['cat', 'eat', 'dare', 'bash', 'tea', 'dear', 'read']))
    ['dare', 'dear', 'eat', 'read', 'tea']
    """
    all_anagrams = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(set(lst[i]) - set(lst[j])) == 0:
                all_anagrams.add(lst[i])
                all_anagrams.add(lst[j])
    return list(all_anagrams)

# problem - need one item in lst to compare to all rest of list items **

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "ana G!"