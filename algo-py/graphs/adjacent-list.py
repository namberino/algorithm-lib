class Graph:
    # n is number of nodes
    def __init__(self, n, directed = True) -> None:
        self.node_num = n
        self.g_directed = directed

        self.nodes = range(self.node_num)
        self.adj_list = {node: set() for node in self.nodes}

    def add_edge(self, node1, node2, weight = 1):
        self.adj_list[node1].add((node2, weight))

        if not self.g_directed:
            self.adj_list[node2].add((node1, weight))

    def print_adj_list(self):
        for key in self.adj_list.keys():
            if not len(self.adj_list[key]) == 0:
                print(f"node {key}: {self.adj_list[key]}")
            else:
                print(f"node {key}: NULL")


graph = Graph(5, False)

graph.add_edge(0, 0, 25)
graph.add_edge(0, 1, 5)
graph.add_edge(0, 2, 3)
graph.add_edge(1, 3, 1)
graph.add_edge(1, 4, 15)
graph.add_edge(4, 2, 7)
graph.add_edge(4, 3, 11)

graph.print_adj_list()
