graph = {
    1 : [5, 6, 2],
    2 : [1, 6, 4, 3],
    3 : [2, 4],
    4 : [3, 2, 6, 5],
    5 : [1, 6, 4],
    6 : [1, 2, 5, 4]
}

visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0) 
        print(s, end=' -> ')

        # if (s == search_node):
        #     print(f"\nFound {search_node}")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


print("Breadth-first search order: ")
bfs(visited, graph, 1)
