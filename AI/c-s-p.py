# import networkx as nx
# import matplotlib.pyplot as plt

# # Read input from file
# with open('C:\JUSTCODE\AI\input1.txt', 'r') as f:
#     # Read the number of variables
#     n_v = int(f.readline().strip())
    
#     # Create domains for each variable
#     domains = {name: set(range(1, int(size) + 1)) for name, size in [f.readline().strip().split() for _ in range(n_v)]}
    
#     # Read the number of unary constraints
#     n_uc = int(f.readline().strip())
    
#     # Read unary constraints into a list
#     un_cons = [f.readline().strip() for _ in range(n_uc)]
    
#     # Create a modified domains copy
#     mod_domains = domains.copy()
    
#     # Read the number of binary constraints
#     n_bc = int(f.readline().strip())
    
#     # Create labels for binary constraints
#     labels = {(var1, var2): f"{var1} {op} {var2} {arith_op} {int(value)}" for var1, op, var2, arith_op, value in [f.readline().strip().split() for _ in range(n_bc)]}

# # Create a graph
# G = nx.Graph()
# G.add_edges_from(labels.keys(), label="")

# # Modify domains based on unary constraints
# for constraint in un_cons:
#     var, op, value = constraint.split()
#     value = int(value)
    
#     # Apply unary constraint
#     if op == '<':
#         mod_domains[var] = set(x for x in mod_domains[var] if x < value)
#     elif op == '>':
#         mod_domains[var] = set(x for x in mod_domains[var] if x > value)
#     elif op == '<=':
#         mod_domains[var] = set(x for x in mod_domains[var] if x <= value)
#     elif op == '>=':
#         mod_domains[var] = set(x for x in mod_domains[var] if x >= value)
#     elif op == '==':
#         mod_domains[var] = {value}

# # Display original and modified domains
# print("Original Domains:", domains)
# print("Modified Domains:", mod_domains)

# # Visualize the graph with a circular layout
# pos = nx.circular_layout(G)
# plt.figure()
# nx.draw(G, pos, with_labels=True, font_color='black', node_size=500, node_color='pink', edge_color='black', width=1, alpha=0.9, labels={node: node for node in G.nodes()})
# nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='red')
# plt.show()


# //-------------------------------------------

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
labels = {}
un_cons = []

with open('C:\JUSTCODE\AI\input1.txt', 'r') as f:
    n_v = int(f.readline().strip())

    domains = {}
    for i in range(n_v):
        name, domain_size = f.readline().strip().split()
        domains[name] = set(range(1, int(domain_size) + 1))
    mod_domains = domains.copy()
    n_uc = int(f.readline().strip())

    for i in range(n_uc):
        var, op, value = f.readline().strip().split()
        str1 = ""
        str1 += var + " " + op + " " + str(value)
        if str1 not in un_cons:
            un_cons.append(str1)
        value = int(value)
        if op == '<':
            mod_domains[var] = set(x for x in domains[var] if x < value)
        elif op == '>':
            mod_domains[var] = set(x for x in domains[var] if x > value)
        elif op == '<=':
            mod_domains[var] = set(x for x in domains[var] if x <= value)
        elif op == '>=':
            mod_domains[var] = set(x for x in domains[var] if x >= value)
        elif op == '==':
            mod_domains[var] = {value}

    n_bc = int(f.readline().strip())
    for i in range(n_bc):
        var1, op, var2, arith_op, value = f.readline().strip().split()
        value = int(value)
        str1 = ""
        str1 += var1 + " " + op + " " + var2 + " " + arith_op + " " + str(value)
        if str1 not in labels:
            labels[(var1, var2)] = str1
        G.add_node(var1)
        G.add_node(var2)
        G.add_edge(var1, var2, label=str1)

print("The original Domains are: {}".format(domains))
print("The Unary Constraints are: ")
for i in un_cons:
    print(i)
print("The Modified Domains From Unary Constraints are: {}".format(mod_domains))
pos = nx.spring_layout(G)
plt.figure()

nx.draw(
    G, pos, edge_color='black', width=1, linewidths=1,
    node_size=500, node_color='pink', alpha=0.9,
    labels={node: node for node in G.nodes()}
)
print()
print("The Binary Constraints are: ")
for i in labels.values():
    print(i)
print("----")

nx.draw_networkx_edge_labels(
    G, pos,
    edge_labels=labels,
    font_color='red'
)

plt.show()

arcs = []
bin_dom = {}
mod_labels = {}

for key, value in labels.items():
    mod_labels[(key[0].upper(), key[1].upper())] = value

for i in mod_labels.keys():
    str1 = str(i)
    str1 = str1.strip("('").strip("')").split("', '")
    arcs.append(str1)

for key, values in mod_domains.items():
    bin_dom[key.upper()] = list(values)


def arc_consistent(x, y):
    revised = False
    all_constraints = [
        constraint for constraint in mod_labels if constraint[0] == x and constraint[1] == y]
    for x_value in bin_dom[x]:
        satisfies = False
        for y_value in bin_dom[x]:
            for constraint in all_constraints:
                constraint_func = lambda x, y: mod_labels[constraint]
                
                if constraint_func(x_value, y_value):
                    satisfies = True
        if not satisfies:
            bin_dom[x].remove(x_value)
            revised = True

    return revised

def arc_consistent(x, y):
    revised = False
    all_constraints = [
        constraint for constraint in mod_labels if constraint[0] == x and constraint[1] == y]
    for x_value in bin_dom[x]:
        satisfies = False
        for y_value in bin_dom[x]:
            for constraint in all_constraints:
                constraint_func = lambda x, y: mod_labels[constraint]
               
                if constraint_func(x_value, y_value):
                    satisfies = True
        if not satisfies:
            bin_dom[x].remove(x_value)
            revised = True

    return revised


def dom_bin_modify(func_arcs):
    queue = func_arcs[:]
    while queue:
        (x, y) = queue.pop(0)
        arc_consist = arc_consistent(x, y)
        if arc_consist:
            neighbors = [neighbor for neighbor in func_arcs if neighbor[1] == x]
            queue = queue + neighbors


dom_bin_modify(arcs)
print(bin_dom)