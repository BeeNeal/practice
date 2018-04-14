# linked list
# need a head that points to the next item in list, last item in list will point to None
# adding is easiest to head, because will have the head pointer

class Node:

    def __init__(self, data):
        self.data = data
        self.next = none

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, new_data):
        self.data = new_data

    def setNext(self, new_next):
        self.next = new_next


class LinkedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        length = 0
        while self.next:
            length += 1
            

        return length

    def add(self, item):
        new_node = Node(item)
        self.next = self.head
        self.head = self.new_node