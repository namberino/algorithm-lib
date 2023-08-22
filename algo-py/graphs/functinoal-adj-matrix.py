def add_vertex(v):
    global graph
    global vertices_num
    global vertices

    if v in vertices:
        print(f"Vertex {v} already exists")
    else:
        vertices_num = vertices_num + 1
        vertices.append(v)

        if vertices_num > 1:
            for vertex in graph:
                vertex.append(0)
        temp = []

        for i in range(vertices_num):
            temp.append(0)
        graph.append(temp)

# Add an edge between vertex v1 and v2 with edge weight w
def add_edge(v1, v2, w = 1):
    global graph
    global vertices_num
    global vertices

    # Check if vertex v1 is a valid vertex
    if v1 not in vertices:
        print(f"Vertex {v1} does not exist.")
    # Check if vertex v1 is a valid vertex
    elif v2 not in vertices:
        print(f"Vertex {v2} does not exist.")
    else:
        index1 = vertices.index(v1)
        index2 = vertices.index(v2)
        graph[index1][index2] = w

def print_adj_matrix():
    global graph
    global vertices_num

    for i in range(vertices_num):
        for j in range(vertices_num):
            if graph[i][j] != 0:
                print(f"{vertices[i]} -> {vertices[j]}")


vertices = []
vertices_num = 0
graph = []

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

print_adj_matrix()

print("\nMatrix representation:")

for row in graph:
   print(row)
