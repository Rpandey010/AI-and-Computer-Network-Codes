import networkx as nx
import matplotlib.pyplot as plt

# Function to make the graph arc-consistent
def arc_consistent(x, y, mod_domains, mod_labels):
    revised = False
    all_constraints = [constraint for constraint in mod_labels if constraint[0] == x and constraint[1] == y]
    for x_value in mod_domains[x]:
        satisfies = False
        for y_value in mod_domains[y]:
            for constraint in all_constraints:
                constraint_func = lambda x, y: eval(mod_labels[constraint])
                if constraint_func(x_value, y_value):
                    satisfies = True
        if not satisfies:
            mod_domains[x].remove(x_value)
            revised = True
    return revised

# Function to perform arc consistency propagation
def dom_bin_modify(arcs, mod_domains, mod_labels):
    queue = arcs[:]
    while queue:
        (x, y) = queue.pop(0)
        arc_consist = arc_consistent(x, y, mod_domains, mod_labels)
        if arc_consist:
            neighbors = [neighbor for neighbor in arcs if neighbor[1] == x]
            queue = queue + neighbors

# Main function to read input and create constraint graph
def main():
    G = nx.Graph()
    mod_domains = {}
    mod_labels = {}
    arcs = []

    with open('C:\JUSTCODE\AI\input.txt', 'r') as f:
        n_v = int(f.readline().strip())
        for _ in range(n_v):
            name, domain_size = f.readline().strip().split()
            mod_domains[name] = set(range(1, int(domain_size) + 1))

        n_uc = int(f.readline().strip())
        for _ in range(n_uc):
            var, op, value = f.readline().strip().split()
            value = int(value)
            if op == '<':
                mod_domains[var] = set(x for x in mod_domains[var] if x < value)
            elif op == '>':
                mod_domains[var] = set(x for x in mod_domains[var] if x > value)
            elif op == '<=':
                mod_domains[var] = set(x for x in mod_domains[var] if x <= value)
            elif op == '>=':
                mod_domains[var] = set(x for x in mod_domains[var] if x >= value)
            elif op == '==':
                mod_domains[var] = {value}

        n_bc = int(f.readline().strip())
        for _ in range(n_bc):
            var1, op, var2, arith_op, value = f.readline().strip().split()
            value = int(value)
            str1 = f"{var1} {op} {var2} {arith_op} {value}"
            mod_labels[(var1, var2)] = str1
            G.add_node(var1)
            G.add_node(var2)
            G.add_edge(var1, var2, label=str1)
            arcs.append((var1, var2))

    print("Original Domains:", mod_domains)

    print("Unary Constraints:")
    for var, values in mod_domains.items():
        print(f"{var}: {values}")

    print("Binary Constraints:")
    for arc, label in mod_labels.items():
        print(f"{arc[0]} {label} {arc[1]}")

    dom_bin_modify(arcs, mod_domains, mod_labels)
    print("Modified Domains:", mod_domains)

    pos = nx.spring_layout(G)
    plt.figure()

    nx.draw(
        G, pos, edge_color='black', width=1, linewidths=1,
        node_size=500, node_color='pink', alpha=0.9,
        labels={node: node for node in G.nodes()}
    )

    nx.draw_networkx_edge_labels(
        G, pos,
        edge_labels={(var1, var2): label for (var1, var2), label in mod_labels.items()},
        font_color='red'
    )

    plt.show()

if __name__ == "__main__":
    main()
