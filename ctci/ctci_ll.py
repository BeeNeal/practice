class Node(object):
    """Node object for LL"""

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    """Linked List object"""

    def __init__(self):
        self.head = None
        self.tail = None

    def append_node(self, data):
        """add node to end of LL"""

        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        if self.tail:
            self.tail.next = new_node
        
        self.tail = new_node

        # if don't have tail, can do by iterating to end:
        # current_head = self.head
        # if current_head.next:
        #     current_head = current_head.next
        # else:
        #     current_head.next = new_node

    def remove_node(self, data):

        current = self.head

        # check head first so head pointer doesn't get lost
        if current.next and current.data == data:
            current = current.next
            if current is None:
                self.tail = None
            return

        if current.next.data == data:
            try:
                current.next = current.next.next
            # Exception will occur if deleting tail node; can't simply delete
            # tail node, because would delete tail pointer
            except:
                self.tail = current
                current.next = None

    def print_all_nodes(self):
        """
        >>> ll.print_all_nodes()
        a
        b
        c
        """

        current = self.head
        while current:
            print current.data
            current = current.next

    def find_node(self, data):
        """
        >>> ll.find_node('b')
        True
        >>> ll.find_node('z')
        False
        """

        current = self.head
        while current:
            if current.data == data:
                return True
            else:
                current = current.next

        return False

    def remove_node_by_index(self, i):
        """ """

        ind = 1
        current = self.head
        if ind == i:
            current.next = current.next.next
        else:
            current = current.next
            ind += 1


def remove_duplicates(head_node):
    """Given an unsorted linked list, remove the duplicates"""
    
    # iterate through list, add each node to a set, if node is present in set, 
    # remove

    seen = set()
    current = head_node
    while current.next:
        if current in seen:
            current.next = current.next.next


    

def output_cycle_node(head_node):
    """Given a circular linked list, return the node that makes it circular

    >>> circular_ll = LinkedList()
    >>> a = Node('a')
    >>> b = Node('b')
    >>> c = Node('c')
    >>> d = Node('d')
    >>> a.next = b
    >>> b.next = c
    >>> c.next = d
    >>> d.next = b

    >>> circular_ll.head = a
    >>> print output_cycle_node(circular_ll.head)
    d

    """

    slow = head_node
    fast = head_node

    while fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return slow.data


if __name__ == "__main__":
    import doctest

    ll = LinkedList()
    ll.append_node('a')
    ll.append_node('b')
    ll.append_node('c')

    if doctest.testmod().failed == 0:
        print "Linked List champion, tests passed!"



