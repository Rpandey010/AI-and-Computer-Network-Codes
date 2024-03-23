#SENTENCES

# 1. Raja is a man.
# 2. Men are mammals.
# 3. Mammals are animals.
# 4. All animals are mortal.
# 5. Men have two legs and one nose.
# 6. Men likes to drink soda.


import networkx as nx
import matplotlib.pyplot as plt

# Entities and relationships
# entities = ['Raja', 'man', 'mammal', 'animal', 'leg', 'nose', 'soda']
# relationships = [
#     ('Raja', 'man', 'is a'),
#     ('man', 'mammal', 'are'),
#     ('mammal', 'animal', 'are'),
#     ('animal', 'mortal', 'are'),
#     ('man', 'leg', 'have'),
#     ('man', 'nose', 'have'),
#     ('man', 'soda', 'like to drink')
# ]

# Another example
entities = ['Jerry', 'cat', 'mammal', 'animal', 'leg', 'milk', 'mortal']
relationships = [
    ('Jerry', 'cat', 'is a'),
    ('cat', 'mammal', 'are'),
    ('mammal', 'animal', 'are'),
    ('animal', 'mortal', 'are'),
    ('cat', 'leg', 'have'),
    ('cat', 'milk', 'like to drink')
]

# Creatinggg a multigraph
G = nx.MultiDiGraph()

# Adding the nodes
for entity in entities:
    G.add_node(entity)

# Adding the edges
for relationship in relationships:
    G.add_edge(relationship[0], relationship[1], label=relationship[2])

# MULTIGRAPH
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=8, width=1.0)
edge_labels = {(u, v): d['label'] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=6)
plt.show()