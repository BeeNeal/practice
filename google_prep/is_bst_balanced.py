  class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

def is_balanced(root):

    current = root
    seen = set()

    while current:
        if current.value in seen:
            return False
        seen.add(current.value)

class Balanced(object):
    def isValidBST(self, root):
        return self.isvalid(root, float('-inf'), float('inf'))
    
    def isvalid(self, root, low, high):
        if not root:
            return True
        if root.val <= low or root.val >= high:
            return False
        return self.isvalid(root.left, low, root.val) and self.isvalid(root.right, root.val, high)


# The  value of every node in a node's left subtree is less than the data value of that node.
# The  value of every node in a node's right subtree is greater than the data value of that node.
# The  value of every node is distinct.


def is_binary_search_tree(root,
                      lower_bound=-float('inf'),
                      upper_bound=float('inf')):
    """solution using recursion, susceptible to stack overflow"""
    if not root:
        return True

    if root.value >= upper_bound or root.value <= lower_bound:
        return False

    return (is_binary_search_tree(root.left, lower_bound, root.value)
            and is_binary_search_tree(root.right, root.value, upper_bound))


def is_binary_search_tree(root):
    # Start at the root, with an arbitrarily low lower bound
    # and an arbitrarily high upper bound
    node_and_bounds_stack = [(root, -float('inf'), float('inf'))]

    # Depth-first traversal, list unpacking
    while len(node_and_bounds_stack):
        node, lower_bound, upper_bound = node_and_bounds_stack.pop()

        # If this node is invalid, we return false right away
        if (node.value <= lower_bound) or (node.value >= upper_bound):
            return False

        if node.left:
            # This node must be less than the current node
            node_and_bounds_stack.append((node.left, lower_bound, node.value))
        if node.right:
            # This node must be greater than the current node
            node_and_bounds_stack.append((node.right, node.value, upper_bound))

    # If none of the nodes were invalid, return true
    # (at this point we have checked all nodes)
    return True



def is_bst(root):

    nodes_stack = [root, float('-inf'), float('inf')]
    while len(nodes_stack):
        node, lower, upper = nodes_stack.pop()

        if node.value <= lower or node.value >= upper:
            return False

        if node.left:
            # append tuples that will be unpacked into their sep components
            nodes_stack.append((node.left, lower, node.value)
        if node.right:
            nodes_stack.append((node.right, node.value, upper))

    return True



