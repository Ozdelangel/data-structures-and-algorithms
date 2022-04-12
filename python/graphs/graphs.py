from code_challenges.stack_and_queue.queue import Queue
from code_challenges.stack_and_queue.stack import Stack


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self,value):
        v = Vertex(value)
        self.adjacency_list[v] = []
        return v

    def add_edge(self, vertex1, vertex2, weight=0):
       edge = Edge(vertex2, weight)
       self.adjacency_list[vertex1].append(edge)

    def get_node(self):
       return list(self.adjacency_list.keys())

    def get_neighbors(self,vertex):
        return self.adjacency_list[vertex]

    def size(self):
        return len(self.adjacency_list)

    def breadth_first(self,vertex):
        node = []
        breadth = Queue()
        visited = {}
        breadth.enqueue(vertex)
        visited.add(vertex)
        while breadth is not None:
            if vertex is not visited:
                visited.add(vertex)
                breadth.enqueue(vertex)
            return node
    def depth_first(self, vertex):
        pass
        stack = Stack()
        visited = set()
        stack.push(vertex)
        while (len(stack)):
            stack.pop()
        if (not visited[vertex]):
            stack.push(vertex)
        for node in self.adjacency_list[vertex]:
            if (not visited[node]):
                stack.push(node)





class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, vertex, weight=1):
        self.vertex = vertex
        self.weight = weight
