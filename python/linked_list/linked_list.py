class Node:
    def __init__(self, value,key, next=None, ):
        self.value = value
        self.next = next
        self.key = key


class LinkedList:
    def __init__(self,head=None):
        self.head = None
        self.next = next

    def insert(self, value):
        self.head = Node(value,self.head)


    def includes(self, value):
        current = self.head
        while current != None:
            if current.value == value:
                return True
            current = current.next
        return False
    # had help from this website https://www.educative.io/edpresso/what-is-the-str-method-in-python and learned about the to string method and this node too https://stackoverflow.com/questions/20875150/how-to-fill-an-empty-string-which-has-already-been-created-in-python
    def __str__(self):
        current = self.head
        new_string = ''
        while current != None:
            new_string = new_string + (f'{current.value}')
        print(new_string)




