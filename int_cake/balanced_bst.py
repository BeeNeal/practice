class Node(object):

    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None

    def insert_left(self, data):

        self.left = Node(data)
        return self.left

    def insert_right(self, data):

        self.right = Node(data)
        return self.right


class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    def set_root(self, data):
        self.root = Node(data)

    def insert(self, data):
        if self.root is None:
            self.set_root(data)
        else:
            self.insert_node(self.root, data)

    def insert_node(self, current_node, data):
        if data <= current_node.data:
            if not current_node.left:
                current_node.left = Node(data)
            else:
                self.insert_node(current_node.left, data)

        elif data > current_node.data:
            if not current_node.right:
                current_node.right = Node(data)
            else:
                self.insert_node(current_node.right, data)

    def find_node(self, data):
        """Searches BST and returns True if data is found."""

        self.current = self.root
        if self.current is None:
            return False
        elif self.current == data:
            return True
        else:
            if data < self.current.data:
                self.current = self.current.left
            elif data > self.current.data:
                self.current = self.current.right

def id_bst_balanced(bst):
    """Returns t/f based on if BST is balanced."""

    pass


if __name__ == '__main__':
    # Create sample tree
    bst = BinarySearchTree()
    bst.insert(4)
    bst.insert(3)
    bst.insert(7)
    bst.insert(5)
    bst.insert(2)
    bst.insert(6)
    print "searching for 3"
    print bst.find_node(3)
