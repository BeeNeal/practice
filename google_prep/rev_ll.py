class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next  = None

def reverse(head):
    current = head
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

