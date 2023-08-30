import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

G.add_node(1, label='1')
G.add_node(2, label='2')
G.add_node(3, label='3')
G.add_node(4, label='4')
G.add_node(5, label='5')
G.add_node(6, label='6')

G.add_edge(2, 1)
G.add_edge(2, 4)
G.add_edge(3, 2)
G.add_edge(3, 6)
G.add_edge(4, 3)
G.add_edge(4, 6)
G.add_edge(4, 5)
G.add_edge(5, 1)
G.add_edge(6, 1)
G.add_edge(6, 2)
G.add_edge(6, 5)

pos = nx.spring_layout(G)

nx.draw_networkx(G, pos)
nx.draw_networkx_labels(G, pos, labels=nx.get_node_attributes(G, 'label'))

nx.draw_networkx_edges(G, pos)

plt.axis('off')
plt.show()
