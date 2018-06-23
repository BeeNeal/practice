def get_max(stocks):
    """O(n^2) implementation"""

    current_max_profit = 0
    max_profit = 0
    for i in xrange(1, len(stocks)):
        print stocks[-i]
        for j in xrange(1, len(stocks)):
            print stocks[-j]
            if stocks[-i] - stocks[-j] > max_profit:
                max_profit = stocks[-i] - stocks[-j]
    return max_profit


def get_max(stocks):
    """O(n) implementation, greedy approach"""
    if len(stocks) < 2:
        return "Need at least 2 prices to turn a profit!"

    min_price = stocks[0]
    # by initializing max_profit as the first dif instead of zero, we also
    # report back if there was no profit to be made
    max_profit = stocks[1] - stocks[0]

    for current_time in xrange(1, len(stocks)):
        current_price = stocks[current_time]

        potential_profit = current_price - min_price
        max_profit = max(max_profit, potential_profit)
        min_price = min(min_price, current_price)

    return max_profit

stocks = [11, 4, 6, 6, 5]
print get_max(stocks)