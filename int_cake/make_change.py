def coin_splitter(amt, denominations):
    """Given an amount and denominations, return all possible combos"""

    combos = set()
    c = dict()
    # handles when combo can be of all same denom (ex: 4: 1111, 22)
    for d in denominations:
        if amt % d == 0:
            qty = amt / d
            combo = str(d) * qty
            combos.add(combo)

        # elif 

    return combos


print coin_splitter(4, [1, 2, 3])


def pennies_and_dimes(num_coins):
    """Given a coin amount, show all possible combos using pennies and dimes"""

# if know how many dimes used, can add pennies on top of that
    # combos = set()

    # for ndimes in range(num_coins + 1):
    #     npennies = num_coins - ndimes
    #     combos.add(ndimes * 10 + npennies)
    # return combos
    results = set()

    for ndimes in range(num_coins + 1):
        npennies = num_coins - ndimes
        results.add(ndimes * 10 + npennies)

    return results

print pennies_and_dimes(10)