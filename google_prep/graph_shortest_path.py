import collections
import itertools as IT

def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

G={'a':['b','c'], 'c':['d']}

# for node1, node2 in IT.combinations(list('abcd'), 2):
#     print('{} -> {}: {}'.format(node1, node2, find_shortest_path(G, node1, node2)))

graphsical = {'a': {'b': 2, 'c': 3},
              'c': {'d': 4, 'e': 3},
              }


def find_longest_path(graph, start, path=[]):
    current_longest_path = 0
    current_path_score = 0
    path = path + [start]  # must put start as list, so can concat

    if start not in graph:
        return None
    else:
        print 'yay'
    # for node in path:
    #     if path

print find_longest_path(graphsical, 'a')

# problem here: can't initialize the scores/path and also recurse...

def get_sum_rec(lst):
    """return sum of list recursively"""

    if len(lst) == 0:
        return 0
    else:
        return lst[0] + get_sum_rec(lst[1:])

print get_sum_rec([1, 3, 4, 2, 5])