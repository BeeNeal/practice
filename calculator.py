"""Calculator

    >>> calc("+ 1 2")  # 1 + 2
    3

    >>> calc("* 2 + 1 2")  # 2 * (1 + 2)
    6

    >>> calc("+ 9 * 2 3")   # 9 + (2 * 3)
    15

Let's make sure we have non-commutative operators working:

    >>> calc("- 1 2")  # 1 - 2
    -1

    >>> calc("- 9 * 2 3")  # 9 - (2 * 3)
    3

    >>> calc("/ 6 - 4 2")  # 6 / (4 - 2)
    3
"""



def calc(s):
    """Evaluate expression."""

    separated_exp = s.split(" ")
    r = len(separated_exp)
    separated_exp.reverse()
    print separated_exp
    current_exp = []
    operators = (['*', '/', '-', '+'])
    final_total = None
    if not separated_exp:
        return final_total

    for i in range(1, len(s) + 1):
        if separated_exp[-i] in operators:
            print current_exp
            final_total = process_expression(separated_exp.pop(), current_exp)
            break
        else:
            current_exp.append(separated_exp.pop())


def process_expression(operator, current_exp):

    current_exp = [int(num) for num in current_exp]

    if operator == '*':
        print current_exp
        for num in current_exp:
            return reduce(lambda x, y: x * y, current_exp)
    elif operator == '+':
        print current_exp
        return sum(current_exp)
    elif operator == '-':
        print current_exp
        total = current_exp.pop(0)
        for num in current_exp:
            total -= num
        return total
    elif operator == '/':
        print current_exp
        total = current_exp.pop(0)
        for num in current_exp:
            total /= num
        return total



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; WELL-CALCULATED! ***\n"



    print "You're a software engineer! I'm a software engineer!" 
    print "I'm a software engineer!"