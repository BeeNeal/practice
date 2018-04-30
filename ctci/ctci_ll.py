class Node(object):
    """Node object for LL"""

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    """Linked List object"""

    def __init__(self):
        self.head = None

    def add_node(self, item):

        new_node = Node(item)
        self.head.next = new_node

    def remove_node(self, item):

        pass

    def print_all_nodes(self):

        current = self.head
        while current:
            print current.data
            current = current.next

    def find_node(self, item):

        current = self.head
        if current.data == item:
            return True
        else:
            current = current.next

        return False




def remove_duplicates(linked_lst):
    """Given an unsorted linked list, remove the duplicates"""

    # iterate through list, add each node to a set, if node is present in set, 
    # remove
    
