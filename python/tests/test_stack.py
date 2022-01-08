# from code_challenges import stack_and_queue
from code_challenges.stack_and_queue.stack import Stack
from code_challenges.stack_and_queue.node import Node


def test_push_to_stack():
    stack = Stack()
    stack.push(1)
    assert stack.peek() == 1
