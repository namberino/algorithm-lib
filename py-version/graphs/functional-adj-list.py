def add_vertex(v):
    global graph
    global vertices_num

    if v in graph:
        print(f"Vertex {v} already exists.")
    else:
        vertices_num += 1
        graph[v] = []

# add an edge between vertex v1 and v2 with edge weight w
def add_edge(v1, v2, w = 1):
    global graph

    # check if vertex v1 is a valid vertex
    if v1 not in graph:
        print(f"Vertex {v1} does not exist.")
    # check if vertex v2 is a valid vertex
    elif v2 not in graph:
        print(f"Vertex {v2} does not exist.")
    else:
        temp = [v2, w]
        graph[v1].append(temp)

def print_adj_list():
    global graph

    for vertex in graph:
        for edges in graph[vertex]:
            print(f"{vertex} -> {edges[0]}")


graph = {}
vertices_num = 0

print("Edges:")
add_vertex(1)
add_vertex(2)
add_vertex(3)
add_vertex(4)
add_vertex(5)
add_vertex(6)

add_edge(2, 1)
add_edge(2, 4)
add_edge(3, 2)
add_edge(3, 6)
add_edge(4, 3)
add_edge(4, 6)
add_edge(4, 5)
add_edge(5, 1)
add_edge(6, 5)
add_edge(6, 2)
add_edge(6, 1)

print_adj_list()

print ("\nList representation:")

for key in graph.keys():
    print(f"{key}: {graph[key]}")
