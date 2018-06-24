lst = ['a', 'b', 'c', 'd', 'e']

import random

def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)

def shuffle(lst):
    if len(lst) <= 1:
        return lst

    last_index = len(lst) - 1

    for i in xrange(0, len(lst) - 1):
        random_choice_index = get_random(i, last_index)

        if random_choice_index != i:
            lst[i], lst[random_choice_index] = lst[random_choice_index], lst[i]
