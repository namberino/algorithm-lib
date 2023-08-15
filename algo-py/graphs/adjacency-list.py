class AdjNode:
    def __init__(self, value):
        self.vertex = value;
        self.next = None;


class Graph:
    def __init__(self, num):
        self.V = num;
        self.graph = [None] * self.V;

    def addEdge(self, s, d):
        node = AdjNode(d);
        node.next = self.graph[s];
        self.graph[s] = node;

        node = AdjNode(s);
        node.next = self.graph[d];
        self.graph[d] = node;

    def printGraph(self):
        for i in range(self.V):
            print("Vertex " + str(i) + ":", end="");
            temp = self.graph[i];
            while temp:
                print(" -> {}".format(temp.vertex), end="");
                temp = temp.next;
            print();


if __name__ == "__main__":
    V = 5;

    graph = Graph(V);
    graph.addEdge(0, 1);
    graph.addEdge(0, 2);
    graph.addEdge(0, 3);
    graph.addEdge(1, 2);

    graph.printGraph();
