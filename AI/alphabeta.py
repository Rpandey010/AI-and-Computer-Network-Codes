# import random

# class Node:
#     def __init__(self, depth, player_num, value=0):
#         self.depth = depth
#         self.player_num = player_num
#         self.value = value
#         self.children = []
#         self.create_children()

#     def create_children(self):
#         if self.depth >= 0:
#             for _ in range(3, 6):
#                 self.children.append(Node(self.depth - 1, -self.player_num, random.randint(-5, 5)))

# def minimax(node, depth, player_num):
#     if depth == 0 or len(node.children) == 0:
#         return node.value

#     if player_num > 0:
#         max_val = float('-inf')
#         for child in node.children:
#             max_val = max(max_val, minimax(child, depth - 1, -player_num))
#         return max_val

#     else:
#         min_val = float('inf')
#         for child in node.children:
#             min_val = min(min_val, minimax(child, depth - 1, -player_num))
#         return min_val

# def alphabeta(node, depth, player_num, alpha, beta):
#     if depth == 0 or len(node.children) == 0:
#         return node.value

#     if player_num > 0:
#         value = float('-inf')
#         for child in node.children:
#             value = max(value, alphabeta(child, depth - 1, -player_num, alpha, beta))
#             alpha = max(alpha, value)
#             if alpha >= beta:
#                 break
#         return value

#     else:
#         value = float('inf')
#         for child in node.children:
#             value = min(value, alphabeta(child, depth - 1, -player_num, alpha, beta))
#             beta = min(beta, value)
#             if beta <= alpha:
#                 break
#         return value

# def main():
#     tree_depth = 3
#     root = Node(tree_depth, 1)
#     print(f"Optimal value (Minimax): {minimax(root, tree_depth, 1)}")
#     print(f"Optimal value (Alpha-Beta): {alphabeta(root, tree_depth, 1, float('-inf'), float('inf'))}")

# if __name__ == "__main__":
#     main()



# //---------------------------------



import random
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, depth, player_num, value=0):
        self.depth = depth
        self.player_num = player_num
        self.value = value
        self.children = []
        self.create_children()

    def create_children(self):
        if self.depth >= 0:
            for _ in range(3, 6):
                self.children.append(Node(self.depth - 1, -self.player_num, random.randint(-5, 5)))

def draw_tree(node, g=None, parent=None, pos=None, x=0, y=0):
    if g is None:
        g = nx.DiGraph()
    g.add_node(x, value=node.value)
    pos[x] = (x, -y)
    if parent is not None:
        g.add_edge(parent, x)
    for child in node.children:
        x, y = draw_tree(child, g, x, pos, x+1, y+1)
    return x, y

def minimax(node, depth, player_num):
    if depth == 0 or len(node.children) == 0:
        return node.value

    if player_num > 0:
        max_val = float('-inf')
        for child in node.children:
            max_val = max(max_val, minimax(child, depth - 1, -player_num))
        return max_val

    else:
        min_val = float('inf')
        for child in node.children:
            min_val = min(min_val, minimax(child, depth - 1, -player_num))
        return min_val

def alphabeta(node, depth, player_num, alpha, beta):
    if depth == 0 or len(node.children) == 0:
        return node.value

    if player_num > 0:
        value = float('-inf')
        for child in node.children:
            value = max(value, alphabeta(child, depth - 1, -player_num, alpha, beta))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value

    else:
        value = float('inf')
        for child in node.children:
            value = min(value, alphabeta(child, depth - 1, -player_num, alpha, beta))
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value

def main():
    tree_depth = 3
    root = Node(tree_depth, 1)
    g = nx.DiGraph()
    pos = {}
    draw_tree(root, g, None, pos)
    labels = {node: g.nodes[node]['value'] for node in g.nodes}
    nx.draw(g, pos, with_labels=True, labels=labels)
    plt.show()
    print(f"Optimal value (Minimax): {minimax(root, tree_depth, 1)}")
    print(f"Optimal value (Alpha-Beta): {alphabeta(root, tree_depth, 1, float('-inf'), float('inf'))}")

if __name__ == "__main__":
    main()