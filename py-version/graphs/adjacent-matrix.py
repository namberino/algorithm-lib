class Graph:
    # n is number of nodes
    def __init__(self, n, directed = True) -> None:
        self.node_num = n
        self.g_directed = directed

        self.adj_matrix = [[0 for column in range(n)] for row in range(n)]

    def add_edge(self, node1, node2, weight = 1):
        self.adj_matrix[node1][node2] = weight

        if not self.g_directed:
            self.adj_matrix[node2][node1] = weight

    def print_adj_matrix(self):
        for row in self.adj_matrix:
            print(row)


graph = Graph(6)

graph.add_edge(1, 1, 25)
graph.add_edge(1, 2, 5)
graph.add_edge(1, 3, 3)
graph.add_edge(2, 4, 1)
graph.add_edge(2, 5, 15)
graph.add_edge(5, 3, 7)
graph.add_edge(5, 4, 11)

graph.print_adj_matrix()
