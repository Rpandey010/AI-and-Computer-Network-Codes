class MultiGraph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = {}

    def add_edge(self, node1, node2, relationship):
        if node1 in self.graph and node2 in self.graph:
            if relationship not in self.graph[node1]:
                self.graph[node1][relationship] = []
            self.graph[node1][relationship].append(node2)

    def has_path(self, start, end, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        if start == end:
            return True
        if start in self.graph:
            for relationship, nodes in self.graph[start].items():
                for node in nodes:
                    if node not in visited:
                        if self.has_path(node, end, visited):
                            return True
        return False

# Create a MultiGraph
graph = MultiGraph()

# Add nodes and edges based on the sentences
entities = ['Raja', 'man', 'men', 'mammals', 'animals', 'nose', 'soda']
relationships = {
    'Raja': [('man', 'is a')],
    'man': [('mammals', 'are'), ('nose', 'have'), ('soda', 'like')],
    'men': [('mammals', 'are')],
    'mammals': [('animals', 'are')],
    'animals': [],
    'nose': [],
    'soda': []
}

for entity in entities:
    graph.add_node(entity)

for node, relations in relationships.items():
    for relation, connected_nodes in relations:
        for connected_node in connected_nodes.split(' and '):
            graph.add_edge(node, connected_node, relation)

# Test if there is a path between two nodes
print(graph.has_path('Raja', 'soda'))  # Output: True
print(graph.has_path('soda', 'Raja'))  # Output: False
