# from code_challenges import stack_and_queue
import queue
from code_challenges.stack_and_queue.stack import Stack
from code_challenges.stack_and_queue.node import Node
from code_challenges.stack_and_queue.queue import Queue


def test_push_to_stack():
    stack = Stack()
    stack.push(5)
    assert stack.top.value == 5
def test_multiple_pushes():
    stack = Stack()
    stack.push(1)
    assert stack.top.value == 1
    stack.push(2)
    assert stack.top.value == 2
    stack.push(3)
    assert stack.top.value == 3
def test_can_pop():
    stack = Stack()
    stack.push(1)
    stack.push(3)
    stack.push(4)
    stack.pop()
    assert stack.top.value == 3
def test_pop_multiples():
    stack = Stack()
    stack.push(1)
    stack.push(4)
    stack.push(3)
    stack.pop()
    stack.pop()
    stack.pop()
    assert stack.top == None
def test_peek():
    stack = Stack()
    stack.push(1)
    stack.push(4)
    stack.push(3)
    assert stack.peek() == 3
def instantiate_empty_stack():
    stack = Stack()
    assert stack.is_empty() == True
def test_pop_and_peek():
    stack = Stack()
    assert stack.pop() == 'this stack is empty'
    assert stack.peek() == 'this stack is empty'
def test_enqueue():
    queue = Queue()
    queue.enqueue(1)
    assert queue.rear.value == 1
def test_multiples_enqueue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(4)
    queue.enqueue(3)
    assert queue.rear.value == 3
def test_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(4)
    queue.enqueue(3)
    queue.dequeue()
    assert queue.front.value == 4
def test_peek_queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(4)
    queue.enqueue(3)
    queue.peek()
    assert queue.peek() == 1
def test_Dequeue_all():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(4)
    queue.enqueue(3)
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    assert queue.front == None
def test_queue_is_empty():
    queue = Queue()
    assert queue.is_empty() == True
def test_dequeue_peek():
    queue = Queue()
    assert queue.dequeue() == 'the queue is empty'
    assert queue.peek() == 'the queue is empty'
