# from code_challenges.stack_and_queue import queue
from code_challenges.stack_and_queue.queue import Queue


def breadth_first(tree):
    list_Values = []
    queue = Queue

    if tree.root is None:
        return list_Values

    queue.enqueue(tree.root)

    while not queue.is_empty():
        dequeue = queue.dequeue()
        list_Values.append(dequeue.value)
        if dequeue.left:
            queue.enqueue(dequeue.left)
        if dequeue.right:
            queue.enqueue(dequeue.right)

    return list_Values
