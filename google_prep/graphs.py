# There are three basic ways to represent a graph in memory (objects and pointers,
#  matrix, and adjacency list), and you should familiarize yourself with each 
# representation and its pros and cons.

# You should know the basic graph traversal algorithms: breadth-first search and 
# depth-first search. You should know their computational complexity, their tradeoffs,
#  and how to implement them in real code.


# NP-complete problems, such as traveling salesman and the knapsack problem

# one of the easiest ways to implement a graph is with a 2D matrix
    # but not a good way to store sparse data

# Good way to store sparse data is with an adjacency list
    # master list of all vertices
    # all vertices these vertices are adjacent to are stored in dictionary

# graph = {'v0':['v1', 'v2'], 'v1', 'v2', 'v3', 'v4'}


# graph = {}
graph = [v0, v1, v2, v3, v4]

v0 = {'id': 'v0', 'adj': {'v1':5, 'v5':2}}
v1 = {'id': 'v1', 'adj': {'v2':4}}
v2 = {'id': 'v2', 'adj': {'v1':4, 'v3':9, 'v5':1}}
v3 = {'id': 'v3', 'adj': {'v2':9, 'v4':7, 'v5':3}}
v4 = {'id': 'v4', 'adj': {'v0':1, 'v3':7, 'v5':8}}
v5 = {'id': 'v5', 'adj': {'v0':1, 'v2': , 'v3':3, 'v4':8}}
