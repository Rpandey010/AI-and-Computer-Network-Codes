#include <iostream>
#include <queue>
#include <vector>

using namespace std;

// Function to perform BFS
void bfs(vector<vector<int>>& graph, int initialNode, int goalNode) {
    int numNodes = graph.size();
    vector<bool> visited(numNodes, false);
    queue<vector<int>> paths;

    // Initialize the queue with the first path starting from initial state
    paths.push({initialNode});

    while (!paths.empty()) {
        // Get the frontmost path from the queue
        vector<int> path = paths.front();
        paths.pop();

        // Get the last node of the current path
        int lastNode = path.back();

        // Check if the last node is the goal node
        if (lastNode == goalNode) {
            // Print the path
            for (int node : path) {
                cout << node << " ";
            }
            cout << endl;
            return;
        }

        // Check all vertices connected to the current node
        for (int i = 0; i < numNodes; i++) {
            if (graph[lastNode][i] == 1 && !visited[i]) {
                // Create a new path from the earlier path and append the vertex
                vector<int> newPath = path;
                newPath.push_back(i);

                // Insert the new path to the queue
                paths.push(newPath);

                // Mark the vertex as visited
                visited[i] = true;
            }
        }
    }
}

int main() {
    // Example adjacency matrix
    vector<vector<int>> graph = {
        {0, 1, 1, 0, 0},
        {1, 0, 0, 1, 0},
        {1, 0, 0, 1, 1},
        {0, 1, 1, 0, 1},
        {0, 0, 1, 1, 0}
    };

    int initialNode = 0;
    int goalNode = 4;

    bfs(graph, initialNode, goalNode);

    return 0;
}