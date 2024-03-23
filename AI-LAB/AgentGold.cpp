#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>

using namespace std;

bool isValid(int x, int y, int N) {
    return 0 <= x && x < N && 0 <= y && y < N;
}

void agentProgram(int N, int X, pair<int, int> chargingStation, pair<int, int>& potOfGold) {
    int x = chargingStation.first;
    int y = chargingStation.second;
    int timeTaken = 0;
    int charge = X;

    vector<vector<bool>> explored(N, vector<bool>(N, false));

    while (charge > 0) {
        //  Simulating the current location of an agent
        cout << "Current location: (" << x << ", " << y << ")" << endl;

        // Checking if the agent found the gold
        if (make_pair(x, y) == potOfGold) {
            cout << "Pot of gold found!" << endl;
            break;
        }

        // If room explored making it true
        explored[x][y] = true;

        // Move the agent based on the rules
        if (isValid(x + 1, y, N) && !explored[x + 1][y]) {
            x = x + 1;  // Move forward
        } else if (isValid(x, y + 1, N) && !explored[x][y + 1]) {
            y = y + 1;  // Move right
        } else if (isValid(x - 1, y, N) && !explored[x - 1][y]) {
            x = x - 1;  // Move backward
        } else if (isValid(x, y - 1, N) && !explored[x][y - 1]) {
            y = y - 1;  // Move left
        } else {
            // If all neighboring rooms are explored, move backward
            x = x - 1;
        }

        // Update charge and time taken
        charge--;
        timeTaken++;
    }

    // Output total time taken
    // Here total time I assumed to be the no. of steps or moves the agent makes 
    // while navigating the grid to find the pot of gold or until it decides to go to the charging station.
    cout << "Total time taken: " << timeTaken << " units" << endl;

    // Output the location where the decision to charge was taken
    cout << "Decision to charge taken at: (" << x << ", " << y << ")" << endl;
}

int main() {
    srand(time(0));  

    // Inputs
    int N, X;
    cout << "Enter the size of the grid (N): ";
    cin >> N;
    cout << "Enter the battery capacity (X): ";
    cin >> X;

    // Charging station location input
    pair<int, int> chargingStation;
    cout << "Enter the charging station location (x y): ";
    cin >> chargingStation.first >> chargingStation.second;

    // Pot of gold location input
    pair<int, int> potOfGold;
    cout << "Enter the pot of gold location (x y): ";
    cin >> potOfGold.first >> potOfGold.second;

    // Run the agent program
    agentProgram(N, X, chargingStation, potOfGold);

    return 0;
}
