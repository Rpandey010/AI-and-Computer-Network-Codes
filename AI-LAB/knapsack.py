def est_profit_heuristic(remaining_capacity, remaining_weights, remaining_profits):
    """
    Estimates the profit for the heuristic approach of the fractional knapsack problem.
    """
    estimated_profit = 0
    remaining_capacity_temp = remaining_capacity

    for weight, profit in zip(remaining_weights, remaining_profits):
        if weight <= remaining_capacity_temp:
            estimated_profit += profit
            remaining_capacity_temp -= weight
        else:
            fraction = remaining_capacity_temp / weight
            estimated_profit += fraction * profit
            break

    return estimated_profit

def knapsack_rec_heuristic(current_index, current_weight, current_profit, capacity, weights, profits, decision_space):
    """
    Recursive function to solve the knapsack problem using a heuristic approach.
    """
    if current_index == len(weights) or current_weight > capacity:
        return current_weight, current_profit, decision_space.copy()

    # Exclude the current item
    weight_exclude, profit_exclude, decision_space_exclude = knapsack_rec_heuristic(
        current_index + 1, current_weight, current_profit, capacity, weights, profits, decision_space.copy()
    )

    # Include the current item
    if current_weight + weights[current_index] <= capacity:
        decision_space[current_index] = 1
        weight_include, profit_include, decision_space_include = knapsack_rec_heuristic(
            current_index + 1, current_weight + weights[current_index], current_profit + profits[current_index],
            capacity, weights, profits, decision_space.copy()
        )
        decision_space[current_index] = 0  # Reset the decision space for backtracking
    else:
        weight_include, profit_include, decision_space_include = current_weight, current_profit, decision_space.copy()

    # Choose the better option
    if profit_exclude > profit_include:
        return weight_exclude, profit_exclude, decision_space_exclude
    else:
        return weight_include, profit_include, decision_space_include

def a_star_knapsack(N, W, weights, profits):
    """
    Solves the knapsack problem using the A* algorithm.
    """
    initial_decision_space = [-1] * N
    result_weight, result_profit, result_decision_space = knapsack_rec_heuristic(
        0, 0, 0, W, weights, profits, initial_decision_space
    )

    # Replace -1 with 0 in the final decision space
    result_decision_space = [0 if decision == -1 else decision for decision in result_decision_space]

    print("Best Weight:", result_weight)
    print("Best Profit:", result_profit)
    print("Best Decision Space:", result_decision_space)

# Example usage:
N = 10
W = 20

weights = [2, 1, 3, 4, 5, 2, 1, 3, 9, 7]
profits = [4, 2, 3, 5, 8, 9, 7, 3, 2, 1]

a_star_knapsack(N, W, weights, profits)
