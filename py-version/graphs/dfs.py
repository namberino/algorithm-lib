from collections import defaultdict

graph = defaultdict(list)
graph['A'] = ['B','S']
graph['S'] = ['C','G']
graph['C'] = ['D', 'E','F']
graph['G'] = ['H']

def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=" ")
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


start_node = 'A'
visited = set()
print("Depth-First Traversal starting from node", start_node)
dfs(graph, start_node, visited)
