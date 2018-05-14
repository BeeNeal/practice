
class Stack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def minimum(self):
        


def rev_string(mystr):
    """Takes in string, reverses characters using a stack

    >>> rev_string('abc')
    'cba'

    """

    stack_for_str = Stack()
    for char in mystr:
        stack_for_str.push(char)
    rev_string = ''
    while not stack_for_str.is_empty():
        rev_string += stack_for_str.pop()

    return rev_string


# use a single array to implement 3 stacks


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "yahooz stacks and queues!"