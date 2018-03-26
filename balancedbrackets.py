"""Does a given string have balanced pairs of brackets?

Given a string, return True or False depending on whether the string
contains balanced (), {}, [], and/or <>.

Many of the same test cases from Balance Parens apply to the expanded
problem, with the caveat that they must check all types of brackets.

These are fine::

   >>> has_balanced_brackets("<ok>")
   True

   >>> has_balanced_brackets("<{ok}>")
   True

   >>> has_balanced_brackets("<[{(yay)}]>")
   True

These are invalid, since they have too many open brackets::

   >>> has_balanced_brackets("(Oops!){")
   False

   >>> has_balanced_brackets("{[[This has too many open square brackets.]}")
   False

These are invalid, as they close brackets that weren't open::

   >>> has_balanced_brackets(">")
   False

   >>> has_balanced_brackets("(This has {too many} ) closers. )")
   False

Here's a case where the number of brackets opened matches
the number closed, but in the wrong order::

    >>> has_balanced_brackets("<{Not Ok>}")
    False

If you receive a string with no brackets, consider it balanced::

   >>> has_balanced_brackets("No brackets here!")
   True

"""
def has_balanced_brackets(phrase):
    """Does a given string have balanced pairs of brackets?

    Given a string as input, return True or False depending on whether the
    string contains balanced (), {}, [], and/or <>.
    """

    closed_to_open = {'}': '{', '>': '<', ')': '(', ']': '['}

    seen_brackets = []

    for char in phrase:
        if char in set(closed_to_open.values()):
            seen_brackets.append(char)
        elif char in closed_to_open:
            if seen_brackets == []:
                return False
            elif seen_brackets[-1] == closed_to_open.get(char):
                seen_brackets.pop()
            else:
                return False

    return seen_brackets == []


# the above function is an optimized version of the below function
def has_balanced_brackets_worse(phrase):
    """Does a given string have balanced pairs of brackets?

    Given a string as input, return True or False depending on whether the
    string contains balanced (), {}, [], and/or <>.
    """

    brackets = {'{': '}', '<': '>', '(': ')', '[': ']'}

    open_brackets = []

    # checks to see if count of opening and closing brackets is equal
    # works, but this O(n) runtime is not ideal
    ob = phrase.count('{') + phrase.count('<') + phrase.count('(') + phrase.count('[')
    cb = phrase.count('}') + phrase.count('>') + phrase.count(')') + phrase.count(']')

    if ob != cb:
        return False

    # iterates through phrase, adds open brackets, pops from stack if 
    # corresponding closing bracket is found
    # O(1) runtime
    for char in phrase:
        if char in brackets:
            open_brackets.append(char)
        elif open_brackets and brackets[open_brackets[-1]] == char:
            open_brackets.pop()
        else:
            continue

    if open_brackets:
        return False

    return True

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU CAUGHT ALL THE STRAY BRACKETS!\n"
