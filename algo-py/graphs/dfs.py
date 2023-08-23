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

visited = set() 

def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" -> ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


dfs(visited, graph, 'A')
