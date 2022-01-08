
from code_challenges.stack_and_queue.node import Node

class Stack:
    def __init__(self):
        self.top = None
    def push(self,value):
        node = Node(value)
        node.next = self.top
        self.top = Node
    def pop(self):
        if not self.top:
            raise Exception
    def peek(self):
        return self.top.value

    def is_empty(self):
        return self.top is None

