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

    def append_multiple_nodes(self, *nodes):
        """
        >>> big_ll = LinkedList()
        >>> big_ll.append_multiple_nodes('z', 'y', 'x')
        >>> big_ll.print_all_nodes()
        z
        y
        x
        """

        for item in nodes:
            self.append_node(item)

    def remove_node(self, data):
        """
        >>> ll = LinkedList()
        >>> ll.append_node('a')
        >>> ll.append_node('b')
        >>> ll.append_node('c')
        >>> ll.remove_node('a')
        >>> ll.print_all_nodes()
        b
        c

        """

        current = self.head

        # check head first so head pointer doesn't get lost
        if current.next and current.data == data:
            self.head = current.next
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


def sum_lists(ll1, ll2):
    """
    Given 2 LLs representing reverse ordered nums, return the sum of the 2 nums

    >>> ll1 = LinkedList()
    >>> ll1.append_node(7)
    >>> ll1.append_node(1)
    >>> ll1.append_node(6)
    >>> ll2 = LinkedList()
    >>> ll2.append_node(5)
    >>> ll2.append_node(9)
    >>> ll2.append_node(2)
    >>> sum_lists(ll1, ll2)
    912

    """

    return list_to_int((ll_to_list(ll1))) + list_to_int((ll_to_list(ll2)))

# Need to take 2 LLs -> convert LLs to Lists -> converts lists to single ints


def list_to_int(lst):
    """
    Take in list of ints, return ints joined into 1 int in reverse order
    >>> list_to_int([1, 2, 3])
    321
    """
    lst.reverse()
    s_nums = ''.join(map(str, lst))
    return int(s_nums)


def ll_to_list(ll):
    """Take in LL, return list

    >>> ll1 = LinkedList()
    >>> ll1.append_node(7)
    >>> ll1.append_node(1)
    >>> ll1.append_node(6)
    >>> ll_to_list(ll1)
    [7, 1, 6]

    """

    ll_contents = []

    current = ll.head
    while current:
        ll_contents.append(current.data)
        current = current.next

    return ll_contents
    

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


def is_palindrome(head):
    """Returns true if LL is palindrome.
    >>> pal_ll = LinkedList()
    >>> pal_ll.append_multiple_nodes('r', 'a', 'd', 'a', 'r')
    >>> is_palindrome(pal_ll.head)
    True
    >>> not_pal_ll = LinkedList()
    >>> not_pal_ll.append_multiple_nodes('r', 'a', 'd', 'a')
    >>> is_palindrome(not_pal_ll.head)
    False
    """

    # if doubly linked list, check if head.next and tail.prev always match

    # use a stack! FIFO
    char_stack = []
    current_char = head
    while current_char:
        char_stack.append(current_char.data)
        current_char = current_char.next

    current_char = head
    while current_char:
        if char_stack.pop() == current_char.data:
            current_char = current_char.next
            continue
        else:
            return False
    return True


if __name__ == "__main__":
    import doctest

    ll = LinkedList()
    ll.append_node('a')
    ll.append_node('b')
    ll.append_node('c')

    if doctest.testmod().failed == 0:
        print "Linked List champion, tests passed!"



