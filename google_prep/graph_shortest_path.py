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

for node1, node2 in IT.combinations(list('abcd'), 2):
    print('{} -> {}: {}'.format(node1, node2, find_shortest_path(G, node1, node2)))


def find_longest_path(graph, start, path=[]):
    current_longest_path = 0
    path = path + [start]
