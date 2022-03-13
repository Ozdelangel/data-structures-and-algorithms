from operator import index
from linked_list.linked_list import LinkedList, Node



class Hashtable:


    def __init__(self, size=1024):
        self.size = size
        self.bucket = size *[None]

        # Initializer

    def add(self, key, value):

        self.size += 1
        index = self.hash(key)
        node = self.bucket[index]

        if node is None:
            self.bucket[index] = Node(key,value)
            return


        prev = node
        while node is not None:
            prev = node
            node = node.next

        prev.next = Node(key,value)


        # Add
        # Arguments: key, value
        # Returns: nothing
        # set the key and value pair in the table, handling collisions as needed.
        # Should a given key already exist, replace its value from the value argument given to this method.

    def get(self, key):
        index = self.hash(key)

        node = self.bucket[index]

        while node is not None and node.key != key:
              node = node.next
        if node is None:
            return None
        else:
            return node.value

        # get
        # Arguments: key
        # Returns: Value associated with that key in the table

    def contains(self, key):
        index = self.hash(key)
        for elem in self.bucket[index]:
            if elem[0] == key:
                return True

        return False


    def hash(self, key):

        'Cat'

        'aCt'
        sum = 0

        for ch in key:
            # convert to ascii Cat
            # if first char, multiply by 11
            # if third char multiuply by 7
             sum += ord(ch)
             # C - 67
             # a - 97
             # t - 116

             # sum 280
        primed = sum * 97
        # 27160
        index = primed % self.size

        # 27160 - primed
        # 536

        return index


        # hash
        # Arguments: key
        # Returns: Index in the collection for that key

    def keys(self, key):
        return self.keys

        # keys
        # Returns: Collection of keys
