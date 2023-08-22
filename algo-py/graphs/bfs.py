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
    out = ""
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0) 
        out += s + ' '

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

    out = out[:-1]
    print(out.replace(' ', ' -> '))


print("Breadth-first search order: ")
bfs(visited, graph, 'A')
