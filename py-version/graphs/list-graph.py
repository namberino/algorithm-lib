class Graph:
    # n is number of nodes
    def __init__(self, n, directed = True) -> None:
        self.node_nums = n
        self.g_directed = directed
        self.list_of_edges = []

    def add_edge(self, node1, node2, weight = 1):
        self.list_of_edges.append([node1, node2, weight])

        if not self.g_directed:
            self.list_of_edges.append([node1, node2, weight])

    def print_edge_list(self):
        edge_nums = len(self.list_of_edges)
        for i in range(edge_nums):
            print(f"edge {i + 1}: {self.list_of_edges[i]}")


graph = Graph(5)

graph.add_edge(0, 0, 25)
graph.add_edge(0, 1, 5)
graph.add_edge(0, 2, 3)
graph.add_edge(1, 3, 1)
graph.add_edge(1, 4, 15)
graph.add_edge(4, 2, 7)
graph.add_edge(4, 3, 11)

graph.print_edge_list()
