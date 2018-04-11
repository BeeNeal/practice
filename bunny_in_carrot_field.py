# you have a bunny & a field of carrots (NxM matrix), put the bunny in the center
# (if there is no clear center pick the space with most carrots nearest the center)
# The bunny can go up down left right and will always go to the adjacent block with

# Clarifying Qs - what is meant by 'cant'?
# We'll start by seeing how many carrots it can eat directly adjacent

# [1, 2, 2, 3, 2]
# [1, 2, 2, 3, 2]
# [1, 2, x, 3, 2]
# [1, 2, 2, 3, 3]

from random import choice

def find_num_carrots(n, m):
    """take in n x m matrix, put bunny in center, return amt carrots eaten"""

    # first draw the matrix, populated with random #s 0-4 (carrots) 
    # write helper function to place bunny in center
    # figure out L R U D how many carrots it can eat

def generate_field(n, m):
    """Take in coordinates of matrix, generate field populated with carrots"""

    field = [[choice(range(5)) for x in range(n)] for y in range(m)] 
    return field


def place_bunny_in_center():
    """ """

    if n % 2 == 0:
        if field[]
    else:
        center_x = n/2

    if m % 2 == 0:
        pass
    else:
        center_y = m/2
find_num_carrots(4, 5)