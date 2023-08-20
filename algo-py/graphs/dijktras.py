class Graph:
    def __init__(self, vertices) -> None:
        self.V = vertices
        self.graph = [[0 for i in range(self.V)] for i in range(self.V)]

    def addEdge(self, u, v, w):
        # u is starting vertex, v is destination vertex, w is weight
        self.graph[u][v] = w 
        self.graph[v][u] = w

    def findMinDist(self, dist, visited):
        minDist = float('inf')
        minDistVertex = -1

        for v in range(self.V):
            if not visited[v] and dist[v] < minDist:
                minDist = dist[v]
                minDistVertex = v

        return minDistVertex

    def dijkstraAlgorithm(self, s):
        # s is the root vertex
        dist = [float('inf')] * self.V
        visited = [False] * self.V

        dist[s] = 0

        for i in range(self.V):
            u = self.findMinDist(dist, visited)
            visited[u] = True

            for v in range(self.V):
                if not visited[v] and self.graph[u][v] > 0:
                    if dist[u] + self.graph[u][v] < dist[v]:
                        dist[v] = dist[u] + self.graph[u][v]

        print("Vertex and Distance from source s")
        for i in range(self.V):
            print(f"{i} \t {dist[i]}")


graph = Graph(7)
graph.addEdge(0, 1, 4)
graph.addEdge(0, 2, 5)
graph.addEdge(0, 3, 2)
graph.addEdge(0, 4, 8)
graph.addEdge(2, 4, 3)
graph.addEdge(3, 1, 1)
graph.addEdge(3, 5, 4)
graph.addEdge(5, 4, 1)
graph.addEdge(6, 0, 0)

graph.dijkstraAlgorithm(0)
