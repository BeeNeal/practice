# anagram puzzle

# doesn't quite work this way because of examples like 'baab'
# def is_anagram_of_palindrome(word):
#     """
#     >>> is_anagram_of_palindrome("a")
#     True

#     >>> is_anagram_of_palindrome("ab")
#     False

#     >>> is_anagram_of_palindrome("aab")
#     True

#     >>> is_anagram_of_palindrome("baab")
#     True

#     >>> is_anagram_of_palindrome("arceace")
#     True

#     >>> is_anagram_of_palindrome("arceaceb")
#     False

#     >>> is_anagram_of_palindrome("aaac")
#     False

#     >>> is_anagram_of_palindrome("aaacaaa")
#     True

#     >>> is_anagram_of_palindrome("aaaacaaa")
#     False
#     """

#     lword = list(word)
#     sword = set(lword)

#     if len(sword) == 2 and len(lword) % 2 == 0:
#         return False

#     if (len(sword) * 2) - len(lword) <= 1:
#         return True

#     return False

def is_anagram_of_pal(word):
    """
    >>> is_anagram_of_pal("a")
    True

    >>> is_anagram_of_pal("ab")
    False

    >>> is_anagram_of_pal("aab")
    True

    >>> is_anagram_of_pal("baab")
    True

    >>> is_anagram_of_pal("arceace")
    True

    >>> is_anagram_of_pal("arceaceb")
    False

    >>> is_anagram_of_pal("aaac")
    False

    >>> is_anagram_of_pal("aaacaaa")
    True

    >>> is_anagram_of_pal("aaaacaaa")
    False
    """

    d = {}
    for char in word:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1

    check = 0
    for amt in d.values():
        if amt % 2 != 0:
            check += 1
        if check > 1:
            return False

    return True


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"
