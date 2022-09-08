from .queue import Queue

class Graph:
    """
    Put docstring here
    """

    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, value):
        new_vertex = Vertex(value)
        self.adjacency_list[new_vertex] = []
        return new_vertex

    def add_edge(self, start_vertex, end_vertex, weight=0):
        edge = Edge(end_vertex, weight)
        if end_vertex not in self.adjacency_list:
            raise KeyError
        self.adjacency_list[start_vertex].append(edge)

    def get_nodes(self):
        return list(self.adjacency_list.keys())

    def get_neighbors(self, vertex):
        return self.adjacency_list[vertex]

    def size(self):
        return len(self.adjacency_list)

    def breadth_first(self, root):

        if root == None:
            return None

        nodes = []
        breadth = Queue()
        visited = set()

        breadth.enqueue(root)
        visited.add(root)

        while breadth.is_empty() == False:
            front = breadth.dequeue()
            nodes.append(front.value)

            for child in self.get_neighbors(front):

                if child.vertex not in visited:
                    visited.add(child.vertex)
                    breadth.enqueue(child.vertex)


        return nodes




class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__ (self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
