class Graph():
	def __init__(self, vertices):
		self.vertices = vertices
		self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

	def print_paths(self, dist):
		print("Vertex and distance from source")
		for node in range(self.vertices):
			print(node + 1, "\t\t", dist[node])

	def min_dist(self, dist, sptSet):
		min = 1e7

		for v in range(self.vertices):
			if dist[v] < min and sptSet[v] == False:
				min = dist[v]
				min_index = v

		return min_index

	def dijkstra(self, source):
		dist = [1e7] * self.vertices
		dist[source] = 0
		sptSet = [False] * self.vertices

		for cout in range(self.vertices):
			u = self.min_dist(dist, sptSet)
			sptSet[u] = True

			for v in range(self.vertices):
				if (self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]):
					dist[v] = dist[u] + self.graph[u][v]

		self.print_paths(dist)


g = Graph(6)

g.graph = [
	[0, 16, 0, 0, 19, 21],
    [16, 0, 5, 6, 0, 11],
    [0, 5, 0, 10, 0, 0],
    [0, 6, 10, 0, 18, 14],
    [19, 0, 0, 18, 0, 33],
    [21, 11, 0, 14, 33, 0]
]

g.dijkstra(0)
