class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next  = None

def reverse(head):
    current_node = head
    previous = None
    next_node = None

    while current:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node

    return previous_node



        1 -> 2 -> 3

        3 -> 2 -> 1


def reverse(head):

    current = head
    previous = None
    next_node = None

    while current:
        # set a temp next_node as the next elem
        next_node = current.next
        # overwrite the current.next to be previous elem, this is the change in pointer
        current.next = previous  # first pass will be None, because now end of ll 
        # previous is now current, 
        previous = current 
        # move to the next item in the ll, what was originally next
        current = next_node
