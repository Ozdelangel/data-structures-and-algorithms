
from code_challenges.stack_and_queue.node import Node
import sys

class Queue:
    def __init__(self,front=None):
        self.front = front
        self.rear = None
    def enqueue(self, value):
        node = Node(value)
        if self.rear is None:
            self.front = node
            self.rear = self.front
        else:
            self.rear.next = node
            self.rear = node
    def dequeue(self):
        try:
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp.value
        except AttributeError:
          return('the queue is empty')
    def peek(self):
        try:
            return self.front.value
        except AttributeError:
            return('the queue is empty')
    def is_empty(self):
        return self.front == None
