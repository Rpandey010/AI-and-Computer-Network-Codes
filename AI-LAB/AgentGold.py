

import random

def is_valid(x, y, N):
    return 0 <= x < N and 0 <= y < N

def agent_program(N, X, charging_station, pot_of_gold):
    x, y = charging_station
    time_taken = 0
    charge = X

    explored = [[False for _ in range(N)] for _ in range(N)]

    while charge > 0:
        # Simulating the current location of an agent
        print(f"Current location: ({x}, {y})")

        # Checking whether Gold Found by an agent
        if (x, y) == pot_of_gold:
            print("GOLD found !!")
            break

        # If room explored making it true
        explored[x][y] = True

        # Move the agent based on the rules
        if is_valid(x + 1, y, N) and not explored[x + 1][y]:
            x = x + 1  # Move forward
        elif is_valid(x, y + 1, N) and not explored[x][y + 1]:
            y = y + 1  # Move right
        elif is_valid(x - 1, y, N) and not explored[x - 1][y]:
            x = x - 1  # Move backward
        elif is_valid(x, y - 1, N) and not explored[x][y - 1]:
            y = y - 1  # Move left
        else:
            # If all neighboring rooms are explored, move backward
            x = x - 1

        # Update charge and time taken
        charge -= 1
        time_taken += 1

    # Output total time taken (number of steps/moves- 1 step- 1 unit time taken)
    # Here total time I assumed to be the no. of steps or moves the agent makes 
    #while navigating the grid to find the pot of gold or until it decides to go to the charging station.
    print(f"Total time taken: {time_taken} units")

    # Output the location where the decision to charge was taken
    print(f"Decision to charge taken at: ({x}, {y})")

if __name__ == "__main__":
    random.seed()  

    # Inputs
    N = int(input("GRID SIZE (N): "))
    X = int(input("CAPACITY OF BATTERY (X): "))

    # Charging station location input
    charging_station = tuple(map(int, input("CHARGING STATION LOCATION (x y): ").split()))

    # Pot of gold location input
    pot_of_gold = tuple(map(int, input("GOLD POT LOACTION (x y): ").split()))

    # Agent Program
    agent_program(N, X, charging_station, pot_of_gold)
