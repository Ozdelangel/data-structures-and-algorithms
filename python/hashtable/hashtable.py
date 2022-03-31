from operator import index
from linked_list.linked_list import Node



class Hashtable:


    def __init__(self, size=1024):
        self.size = size
        self.bucket = size *[None]

        # Initializer

    def set(self, key, value):
        index = self.hash(key)
        node_a = Node(key,value)
        node = self.bucket[index]
        if node is None:
            self.bucket[index] = node_a
            return

        previous = node
        while node is not None:
            previous = node
            node = node.next
        previous.next = Node(key,value)





        # Add
        # Arguments: key, value
        # Returns: nothing
        # set the key and value pair in the table, handling collisions as needed.
        # Should a given key already exist, replace its value from the value argument given to this method.

    def get(self, key):
        index = self.hash(key)

        node = self.bucket[index]

        while node.next is not None:
              node = node.next
        if node is None:
            return None
        else:
            return None



    def contains(self, key):
        index = self.hash(key)
        node = self.bucket[index]
        if node == None:
            return False
        while node is not None:
            if key == node.key:
                node = node.next
                return True
            else:
                node = node.next
                return False


    def hash(self, key):

        sum = 0

        for ch in key:

             sum += ord(ch)

        primed = sum * 97

        index = primed % self.size



        return index




    def keys(self, key):
       keys = []
       for i in self.bucket:
           if i is not None:
               keys.append(i.key)
       return keys

        # keys
        # Returns: Collection of keys
