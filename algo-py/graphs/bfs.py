graph = {
    'A' : ['B', 'S'],
    'B' : ['A'],
    'S' : ['A', 'C', 'G'],
    'C' : ['S', 'D', 'E', 'F'],
    'D' : ['C'],
    'E' : ['C'],
    'F' : ['C', 'G'],
    'G' : ['S', 'F', 'H'],
    'H' : ['G']
}

visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0) 
        print(s, end=" -> ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


print("Breadth-first search order: ")
bfs(visited, graph, 'A')
