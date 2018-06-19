# This all works if the key is an integer, but what about other types of immutables?
#  Use ord? but that would be O(n) for the key

class HashTable(object):
    """Dictionary object"""

    def __init__(self):
        self.size = 11  # size is prime for most efficient collision resolution
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):

        hash_value = self.hash_function(key, len(self.slots))
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data  # overwrite key if already there
            else:
                next_slot = self.rehash(hash_value, len(self.slots))
                times_reslot = 0
                while self.next_slot is not None and self.next_slot != key:
                    next_slot = self.rehash(hash_value, len(self.slots))
                    times_reslot += 1

            if self.slots[next_slot] is None:
                self.slots[next_slot] = key
                self.data[next_slot] = data
            else:
                self.data[next_slot] = data

    def hash_function(self, key, size):
        """In this case we assume our keys will be integers"""

        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size