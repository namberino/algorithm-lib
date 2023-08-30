import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node(1, label='A')
G.add_node(2, label='B')
G.add_node(3, label='C')
G.add_node(4, label='D')
G.add_node(5, label='E')
G.add_node(6, label='F')
G.add_node(7, label='G')
G.add_node(8, label='H')
G.add_node(9, label='S')

G.add_edge(1, 2, weight=1)
G.add_edge(1, 9, weight=1)
G.add_edge(9, 3, weight=1)
G.add_edge(9, 7, weight=1)
G.add_edge(3, 4, weight=1)
G.add_edge(3, 5, weight=1)
G.add_edge(3, 6, weight=1)
G.add_edge(6, 7, weight=1)
G.add_edge(7, 8, weight=1)

pos = nx.spring_layout(G)

# Draw nodes and labels
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_labels(G, pos, labels=nx.get_node_attributes(G, 'label'))

# Draw edges with weights
# edge_labels = nx.get_edge_attributes(G, 'weight')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
nx.draw_networkx_edges(G, pos)

# Show graph
plt.axis('on')
plt.show()
