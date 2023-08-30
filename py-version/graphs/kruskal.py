# Breadth-first
graph = {
    1 : [5, 6, 2],
    5 : [6, 4],
    6 : [2, 4],
    2 : [4, 3],
    4 : [3],
    3 : []
}

# Depth-first
graph = {
    1 : [5, 6, 2],
    2 : [4, 3, 6],
    3 : [4],
    4 : [6, 5],
    6 : [5],
    5 : []
}

class DisjointSet:
    def __init__(self, vertices) -> None:
        self.vertices = vertices
        self.parent = {}

        for vertex in vertices:
            self.parent[vertex] = vertex

        self.rank = dict.fromkeys(vertices, 0)

    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            return self.find(self.parent[item])
        
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)

        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1

class Graph:
    def __init__(self, vertices) -> None:
        self.vertices = vertices
        self.graph = []
        self.nodes = []
        self.mst = []

    def add_edge(self, node1, node2, weight):
        self.graph.append([node1, node2, weight])
        self.graph.append([node2, node1, weight])

    def add_node(self, value):
        self.nodes.append(value)

    def print_kruskal_solution(self, node1, node2, weight):
        for node1, node2, weight in self.mst:
            print(f"{node1} - {node2}: {weight}")

    def kruskal(self):
        dst = DisjointSet(self.nodes)
        i = e = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])

        while e < self.vertices - 1:
            node1, node2, weight = self.graph[i]
            i += 1

            x = dst.find(node1)
            y = dst.find(node2)

            if x != y:
                e += 1
                self.mst.append([node1, node2, weight])
                dst.union(x, y)
        
        self.print_kruskal_solution(node1, node2, weight)


graph = Graph(6)

graph.add_node(1)
graph.add_node(2)
graph.add_node(3)
graph.add_node(4)
graph.add_node(5)
graph.add_node(6)

graph.add_edge(1, 5, 19)
graph.add_edge(1, 6, 21)
graph.add_edge(1, 2, 16)
graph.add_edge(2, 4, 6)
graph.add_edge(2, 3, 5)
graph.add_edge(2, 6, 11)
graph.add_edge(3, 4, 10)
graph.add_edge(4, 6, 14)
graph.add_edge(4, 5, 18)
graph.add_edge(6, 5, 33)

# graph.add_edge(1, 5, 19)
# graph.add_edge(1, 6, 21)
# graph.add_edge(1, 2, 16)
# graph.add_edge(5, 6, 33)
# graph.add_edge(5, 4, 18)
# graph.add_edge(6, 2, 11)
# graph.add_edge(6, 4, 14)
# graph.add_edge(2, 4, 6)
# graph.add_edge(2, 3, 5)
# graph.add_edge(4, 3, 10)

graph.kruskal()
