
class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, vertex,weight=1):
        self.vertex = vertex
        self.weight = weight

class Graph:

    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, value):
        v = Vertex(value)
        self.adjacency_list[v] = []
        return v

    def add_edge(self, node, adj=None, weight=1):
        if node in self.adjacency_list.keys():
            edge_to = Edge(adj, weight)
            self.adjacency_list[node].append(edge_to)
        if adj is not None:
            edge_back = Edge(node, weight)
            self.adjacency_list[adj].append(edge_back)


    def get_nodes(self):
        return list(self.adjacency_list.keys())
            
    def get_neighbor(self, node=None):
        if node:
            return self.adjacency_list[node]
        else:
            return None

    def size(self):
        return len(self.adjacency_list.keys())

    def breadth_first(self, node=None):
        nodes = []
        queue = []
        visited = set()

        queue.append(node)
        visited.add(node)

        while len(queue) > 0:
            front = queue.pop(0)
            nodes.append(front.value)

            for i in self.get_neighbor(front):
                if i.vertex not in visited:
                    visited.add(i.vertex)
                    queue.append(i.vertex)

        return nodes

    def depth_first(self, node=None):

        if node is None: return []

        nodes = []
        stack = []
        visited = set()

        stack.append(node)
        visited.add(node)

        while stack:
            top = stack.pop()
            nodes.append(top.value)

            for i in reversed(self.get_neighbor(top)):
                if i.vertex not in visited:
                    visited.add(i.vertex)
                    stack.append(i.vertex)

        return nodes