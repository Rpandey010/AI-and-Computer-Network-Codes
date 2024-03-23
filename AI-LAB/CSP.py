# import networkx as nx
# import matplotlib.pyplot as plt

# # Step 1: Read Input
# def read_input():
#     N_V = int(input("Enter the total number of variables: "))
#     variables = input("Enter variable names separated by space: ").split()
#     domains = {}
#     for var in variables:
#         domain = input(f"Enter domain for variable {var}: ").split()
#         domains[var] = list(map(int, domain))
    
#     N_UC = int(input("Enter the total number of unary constraints: "))
#     unary_constraints = [input("Enter unary constraint: ").split() for _ in range(N_UC)]
    
#     N_BC = int(input("Enter the total number of binary constraints: "))
#     binary_constraints = [input("Enter binary constraint: ").split() for _ in range(N_BC)]
    
#     return N_V, variables, domains, N_UC, unary_constraints, N_BC, binary_constraints

# # Step 2: Adjust Unary Constraints
# def adjust_unary_constraints(variables, domains, unary_constraints):
#     for constraint in unary_constraints:
#         var, op, value = constraint
#         value = int(value)
#         if op == "<":
#             domains[var] = [d for d in domains[var] if d < value]
#         elif op == ">":
#             domains[var] = [d for d in domains[var] if d > value]
#         elif op == "<=":
#             domains[var] = [d for d in domains[var] if d <= value]
#         elif op == ">=":
#             domains[var] = [d for d in domains[var] if d >= value]
#         elif op == "==":
#             domains[var] = [d for d in domains[var] if d == value]

# # Step 3: Read Binary Constraints (No need for adjustment here)
# # Step 4: Construct Initial Constraint Graph
# def construct_constraint_graph(variables, binary_constraints):
#     G = nx.Graph()
#     G.add_nodes_from(variables)
#     for constraint in binary_constraints:
#         var1, op, var2, arith_op, value = constraint
#         G.add_edge(var1, var2)
#     return G

# # Step 5: Adjust Domains Based on Binary Constraints
# def adjust_domains_binary_constraints(domains, binary_constraints):
#     for constraint in binary_constraints:
#         var1, op, var2, arith_op, value = constraint
#         value = int(value)
#         if arith_op == "+":
#             if op == ">":
#                 domains[var1] = [d for d in domains[var1] if d > domains[var2][0] - value]
#             elif op == "<":
#                 domains[var1] = [d for d in domains[var1] if d < domains[var2][0] - value]
#             elif op == ">=":
#                 domains[var1] = [d for d in domains[var1] if d >= domains[var2][0] - value]
#             elif op == "<=":
#                 domains[var1] = [d for d in domains[var1] if d <= domains[var2][0] - value]
#         elif arith_op == "-":
#             if op == ">":
#                 domains[var1] = [d for d in domains[var1] if d > value - domains[var2][0]]
#             elif op == "<":
#                 domains[var1] = [d for d in domains[var1] if d < value - domains[var2][0]]
#             elif op == ">=":
#                 domains[var1] = [d for d in domains[var1] if d >= value - domains[var2][0]]
#             elif op == "<=":
#                 domains[var1] = [d for d in domains[var1] if d <= value - domains[var2][0]]

# # Step 6: Update Constraint Graph
# def update_constraint_graph(G, domains, binary_constraints):
#     for constraint in binary_constraints:
#         var1, _, var2, _, _ = constraint
#         G[var1][var2]['weight'] = len(domains[var1]) * len(domains[var2])

# # Step 7: Draw Constraint Graph
# def draw_constraint_graph(G, domains):
#     pos = nx.spring_layout(G)
#     plt.figure(figsize=(8, 6))

#     for var in domains:
#         domain_str = ', '.join(map(str, domains[var]))
#         plt.text(pos[var][0], pos[var][1], f"{var}: {domain_str}", bbox=dict(facecolor='lightblue', alpha=0.5), horizontalalignment='center')

#     nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightgray', font_size=12, font_weight='bold', width=2)
#     plt.title("Constraint Graph with Adjusted Domains")
#     plt.show()

# # Main function
# def main():
#     N_V, variables, domains, N_UC, unary_constraints, N_BC, binary_constraints = read_input()

#     adjust_unary_constraints(variables, domains, unary_constraints)

#     G = construct_constraint_graph(variables, binary_constraints)

#     adjust_domains_binary_constraints(domains, binary_constraints)

#     update_constraint_graph(G, domains, binary_constraints)

#     draw_constraint_graph(G, domains)

# if __name__ == "__main__":
#     main()



# //------------------------------------------------
    
# import networkx as nx
# import matplotlib.pyplot as plt

# def read_input():
#     N_V = int(input("Enter the total number of variables: "))
#     variables = input("Enter variable names separated by space: ").split()
#     domains = {}
#     for var in variables:
#         domain = input(f"Enter domain for variable {var}: ").split()
#         domains[var] = list(map(int, domain))
    
#     N_UC = int(input("Enter the total number of unary constraints: "))
#     unary_constraints = [input("Enter unary constraint: ").split() for _ in range(N_UC)]
    
#     N_BC = int(input("Enter the total number of binary constraints: "))
#     binary_constraints = [input("Enter binary constraint: ").split() for _ in range(N_BC)]
    
#     return N_V, variables, domains, N_UC, unary_constraints, N_BC, binary_constraints

# def adjust_unary_constraints(variables, domains, unary_constraints):
#     for constraint in unary_constraints:
#         var, op, value = constraint
#         value = int(value)
#         if op == "<":
#             domains[var] = [d for d in domains[var] if d < value]
#         elif op == ">":
#             domains[var] = [d for d in domains[var] if d > value]
#         elif op == "<=":
#             domains[var] = [d for d in domains[var] if d <= value]
#         elif op == ">=":
#             domains[var] = [d for d in domains[var] if d >= value]
#         elif op == "==":
#             domains[var] = [d for d in domains[var] if d == value]

# def construct_constraint_graph(variables, binary_constraints):
#     G = nx.Graph()
#     G.add_nodes_from(variables)
#     for constraint in binary_constraints:
#         var1, op, var2, arith_op, value = constraint
#         G.add_edge(var1, var2)
#     return G

# def adjust_domains_binary_constraints(domains, binary_constraints):
#     for constraint in binary_constraints:
#         var1, op, var2, arith_op, value = constraint
#         value = int(value)
#         if arith_op == "+":
#             if op == ">":
#                 domains[var2] = [d for d in domains[var2] if d < value - min(domains[var1])]
#             elif op == "<":
#                 domains[var2] = [d for d in domains[var2] if d > value - max(domains[var1])]
#             elif op == ">=":
#                 domains[var2] = [d for d in domains[var2] if d <= value - min(domains[var1])]
#             elif op == "<=":
#                 domains[var2] = [d for d in domains[var2] if d >= value - max(domains[var1])]
#         elif arith_op == "-":
#             if op == ">":
#                 domains[var2] = [d for d in domains[var2] if d < min(domains[var1]) - value]
#             elif op == "<":
#                 domains[var2] = [d for d in domains[var2] if d > max(domains[var1]) - value]
#             elif op == ">=":
#                 domains[var2] = [d for d in domains[var2] if d <= min(domains[var1]) - value]
#             elif op == "<=":
#                 domains[var2] = [d for d in domains[var2] if d >= max(domains[var1]) - value]

# def update_constraint_graph(G, domains, binary_constraints):
#     for constraint in binary_constraints:
#         var1, _, var2, _, _ = constraint
#         G[var1][var2]['weight'] = len(domains[var1]) * len(domains[var2])

# def draw_constraint_graph(G, domains):
#     pos = nx.spring_layout(G)
#     plt.figure(figsize=(8, 6))

#     for var in domains:
#         domain_str = ', '.join(map(str, domains[var]))
#         plt.text(pos[var][0], pos[var][1], f"{var}: {domain_str}", bbox=dict(facecolor='lightblue', alpha=0.5), horizontalalignment='center')

#     nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightgray', font_size=12, font_weight='bold', width=2)
#     plt.title("Constraint Graph with Adjusted Domains")
#     plt.show()

# def main():
#     N_V, variables, domains, N_UC, unary_constraints, N_BC, binary_constraints = read_input()

#     adjust_unary_constraints(variables, domains, unary_constraints)

#     G = construct_constraint_graph(variables, binary_constraints)

#     adjust_domains_binary_constraints(domains, binary_constraints)

#     update_constraint_graph(G, domains, binary_constraints)

#     draw_constraint_graph(G, domains)

# if __name__ == "__main__":
#     main()


# //------------------------------------------------
    
import networkx as nx
import matplotlib.pyplot as plt

def read_input(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        N_V = int(lines[0].strip())
        variables = lines[1].strip().split()
        domains = {}
        for i in range(2, 2 + N_V):
            var, domain = lines[i].strip().split(':')
            domains[var] = list(map(int, domain.split()))
        
        N_UC = int(lines[2 + N_V].strip())
        unary_constraints = [lines[i].strip().split() for i in range(3 + N_V, 3 + N_V + N_UC)]
        
        N_BC = int(lines[3 + N_V + N_UC].strip())
        binary_constraints = [lines[i].strip().split() for i in range(4 + N_V + N_UC, 4 + N_V + N_UC + N_BC)]
    
    return N_V, variables, domains, N_UC, unary_constraints, N_BC, binary_constraints

# ... rest of the code remains the same ...
def adjust_unary_constraints(variables, domains, unary_constraints):
    for constraint in unary_constraints:
        var, op, value = constraint
        value = int(value)
        if op == "<":
            domains[var] = [d for d in domains[var] if d < value]
        elif op == ">":
            domains[var] = [d for d in domains[var] if d > value]
        elif op == "<=":
            domains[var] = [d for d in domains[var] if d <= value]
        elif op == ">=":
            domains[var] = [d for d in domains[var] if d >= value]
        elif op == "==":
            domains[var] = [d for d in domains[var] if d == value]

def construct_constraint_graph(variables, binary_constraints):
    G = nx.Graph()
    G.add_nodes_from(variables)
    for constraint in binary_constraints:
        var1, op, var2, arith_op, value = constraint
        G.add_edge(var1, var2)
    return G

def adjust_domains_binary_constraints(domains, binary_constraints):
    for constraint in binary_constraints:
        var1, op, var2, arith_op, value = constraint
        value = int(value)
        if arith_op == "+":
            if op == ">":
                domains[var2] = [d for d in domains[var2] if d < value - min(domains[var1])]
            elif op == "<":
                domains[var2] = [d for d in domains[var2] if d > value - max(domains[var1])]
            elif op == ">=":
                domains[var2] = [d for d in domains[var2] if d <= value - min(domains[var1])]
            elif op == "<=":
                domains[var2] = [d for d in domains[var2] if d >= value - max(domains[var1])]
        elif arith_op == "-":
            if op == ">":
                domains[var2] = [d for d in domains[var2] if d < min(domains[var1]) - value]
            elif op == "<":
                domains[var2] = [d for d in domains[var2] if d > max(domains[var1]) - value]
            elif op == ">=":
                domains[var2] = [d for d in domains[var2] if d <= min(domains[var1]) - value]
            elif op == "<=":
                domains[var2] = [d for d in domains[var2] if d >= max(domains[var1]) - value]

def update_constraint_graph(G, domains, binary_constraints):
    for constraint in binary_constraints:
        var1, _, var2, _, _ = constraint
        G[var1][var2]['weight'] = len(domains[var1]) * len(domains[var2])

def draw_constraint_graph(G, domains):
    pos = nx.spring_layout(G)
    plt.figure(figsize=(8, 6))

    for var in domains:
        domain_str = ', '.join(map(str, domains[var]))
        plt.text(pos[var][0], pos[var][1], f"{var}: {domain_str}", bbox=dict(facecolor='lightblue', alpha=0.5), horizontalalignment='center')

    nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightgray', font_size=12, font_weight='bold', width=2)
    plt.title("Constraint Graph with Adjusted Domains")
    plt.show()


def main():
    N_V, variables, domains, N_UC, unary_constraints, N_BC, binary_constraints = read_input('AI-LAB/input.txt')

    adjust_unary_constraints(variables, domains, unary_constraints)

    G = construct_constraint_graph(variables, binary_constraints)

    adjust_domains_binary_constraints(domains, binary_constraints)

    update_constraint_graph(G, domains, binary_constraints)

    draw_constraint_graph(G, domains)

if __name__ == "__main__":
    main()