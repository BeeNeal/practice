# #basic tree construction, traversal and manipulation algorithms. You should be
 # familiar with binary trees, n-ary trees, and trie-trees at the very very least. 

# You should be familiar with at least one flavor of balanced binary tree, whether 
# it's a red/black tree, a splay tree or an AVL tree. You should actually know how 
# it's implemented.

# You should know about tree traversal algorithms: BFS and DFS, and know the 
# difference between inorder, postorder and preorder.


class Node(object):

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return "<Node %s l=%s r=%s>" % (self.data, self.left, self.right)

class Tree(object):

    def __init__(self, root):
        """Root should be a root node"""
        
        self.root = root

