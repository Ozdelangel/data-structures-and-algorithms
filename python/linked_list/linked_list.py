class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self,head=None):
        self.head = head
        # ll head of 1
        # (1) -> (2) -> none
        # insert 3
        # (3) -> (1) -> (2) -> None
    def insert(self, value):
        node = Node(value) # will create a node of 3
        if self.head is not None:
           node.next = self.head
        # we say 3's next is the current head which is 1
        # we have to tell the link list that we have a new head
        self.head = node
    def includes(self, x):
        current = self.head
        while current is not None:
            if current.value == x:
                return True
            current = current.next
        return False
    def to_string(self):
        pass

