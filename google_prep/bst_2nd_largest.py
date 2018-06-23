#  Problem - find second largest value in BST

# Notes: I'll aim for O(log n) time, because it's a BST
# BSTs consist of no more than two child nodes per parent, and to the left must 
# be lower to the right must be greater
# So I'll need to find the node that has .right.right = None, and 


class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right


def find_largest_node(root_node):

    if root_node.right:
        return find_largest_node(root_node.right)
    return root_node.value


def find_second_greatest(root):

    # if left subtree, w/o r subtree, second greatest will be largest of l subtree
    current = root
    while current:
        if current.left and not current.right:
            return find_largest_node(current.left)
        if current.right and not current.right.left and not current.right.right:
            return current.value

        current = current.right


def traverse_right(root):

    current = root
    while current.right:
        print current.value
        current = current.right


bst = BinaryTreeNode(6)
# two = BinaryTreeNode(2)
# eight = BinaryTreeNode(8)
# one = BinaryTreeNode(1)
# three = BinaryTreeNode(3)
# ten = BinaryTreeNode(10)
# seven = BinaryTreeNode(7)
# bst.insert_left(two)
# bst.insert_right(eight)
# two.insert_left(one)
# two.insert_right(three)
# eight.insert_right(ten)
# eight.insert_left(seven)

bst.insert_left(2)
bst.insert_right(8)
bst.right.insert_right(10)
bst.right.insert_left(7)
bst.left.insert_left(1)
bst.left.insert_right(3)
bst.right.right.insert_right(11)
bst.right.right.right.insert_right(13)


print find_second_greatest(bst)