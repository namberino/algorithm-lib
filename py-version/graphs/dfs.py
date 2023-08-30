def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


graph = {
    '1': set(['5', '6', '2']),
    '2': set(['1', '6', '4', '3']),
    '3': set(['2', '4']),
    '4': set(['3', '2', '6', '5']),
    '5': set(['1', '6', '4']),
    '6': set(['1', '2', '5', '4'])
}

dfs(graph, '1')
