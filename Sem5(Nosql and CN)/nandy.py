import networkx as nx
import matplotlib.pyplot as plt
import itertools

def lower_bound_cop_number(graph):
    # Initialize the cop positions
    cop_positions = set()

    # Iterate through all nodes and add a cop if it's not already covered by existing cops
    for node in graph.nodes():
        if not any(nx.has_path(graph, cop, node) for cop in cop_positions):
            cop_positions.add(node)

    return len(cop_positions)

def visualize_graph(graph, cops=None, robber=None):
    pos = nx.planar_layout(graph)  # Planar layout for visualization
    nx.draw(graph, pos, with_labels=True, font_weight='bold')

    if cops:
        nx.draw_networkx_nodes(graph, pos, nodelist=cops, node_color='r', node_size=700)

    if robber:
        nx.draw_networkx_nodes(graph, pos, nodelist=[robber], node_color='b', node_size=700)

    plt.show()

def main():
    # Create a strongly connected planar directed graph
    graph = nx.gn_graph(10, create_using=nx.DiGraph())
    graph = nx.strongly_connected_component_subgraphs(graph).__next__()

    # Find a lower bound on the cop number
    lower_bound = lower_bound_cop_number(graph)
    print(f"Lower bound on cop number: {lower_bound}")

    # Visualize the graph
    visualize_graph(graph)

if __name__ == "__main__":
    main()
