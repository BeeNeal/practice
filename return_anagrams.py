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
            print lst[i], lst[j]
            if len(set(lst[i]) - set(lst[j])) == 0:
                all_anagrams.add(lst[i])
                all_anagrams.add(lst[j])
    return list(all_anagrams)

# These loops/combo compare 1 item (at a time) in list to all rest of list items **
 #    cat eat
 #    cat dare
 #    cat bash
 #    cat tea
 #    cat dear
 #    cat read
 #    eat dare
 #    eat bash
 #    eat tea
 #    eat dear
 #    eat read
 #    dare bash
 #    dare tea
 #    dare dear
 #    dare read
 #    bash tea
 #    bash dear
 #    bash read
 #    tea dear
 #    tea read
 #    dear read

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "ana G!"