class Stack:

    def __init__(self):
        self.items = []

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return self.items == []  # if there are items in the list, will return False

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


# Write a function revstring(mystr) that uses a stack to reverse the characters 
# in a string.

def revstring(mystr):
    """reverses the chars in a string using a stack"""

    revstr = Stack()
    for i in range(1, len(mystr) + 1):
        revstr.push(mystr[-i])

    return ''.join(revstr.items)




class Queue:

    def __init__(self):
        self.items = []

    def peek(self):
        pass