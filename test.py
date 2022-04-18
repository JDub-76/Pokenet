
import networkx as nx
import matplotlib.pyplot as plt

g = nx.DiGraph()

g.add_edge('Kingdra', 'Kyogre')
nx.draw(g)

print(g.edges)
print(g.nodes)
plt.show()