from collections import deque

def bfs(adj_matrix, initial_node, goal_node):
    queue = deque([[initial_node]])  # Initialize the queue with the first path starting from initial state
    visited = set()  # Keep track of visited nodes

    while queue:
        path = queue.popleft()  # Get the frontmost path from queue
        last_node = path[-1]  # Get the last node of this path

        if last_node == goal_node:  # Check if the last node is the goal node
            return path  # Return the path if it is the goal node

        if last_node not in visited:  # Check if the node is not visited in the current path
            visited.add(last_node)  # Mark the node as visited

            # Find all nodes connected to the current node in the adjacency matrix
            connected_nodes = [node for node, connected in enumerate(adj_matrix[last_node]) if connected]

            for node in connected_nodes:
                new_path = list(path)  # Create a new path from the earlier path
                new_path.append(node)  # Append the connected node to the new path
                queue.append(new_path)  # Insert the new path to the queue

    return None  # Return None if no path is found

# Example usage
adj_matrix = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 1, 1],
    [0, 1, 1, 0, 1],
    [0, 0, 1, 1, 0]
]

initial_node = 0
goal_node = 4

optimal_path = bfs(adj_matrix, initial_node, goal_node)
if optimal_path:
    print("Optimal path:", optimal_path)
else:
    print("No path found")



