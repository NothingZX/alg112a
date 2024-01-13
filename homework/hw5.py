import numpy as np

def objective_function(x):
    return -(x**2 - 4*x + 4)  # Negative of the function to maximize

def hill_climbing(initial_guess, step_size, max_iterations):
    current_solution = initial_guess

    for iteration in range(1, max_iterations + 1):
        current_value = objective_function(current_solution)
        print(f"Iteration {iteration}: x = {current_solution}, f(x) = {current_value}")

        next_solution = current_solution + step_size
        next_value = objective_function(next_solution)

        if next_value > current_value:
            current_solution = next_solution
        else:
            print("Local maximum reached. Stopping.")
            break

    return current_solution

def main():
    # Example: Maximize the function -(x^2 - 4x + 4) using hill climbing
    initial_guess = 0.0
    step_size = 0.1
    max_iterations = 20

    print("Hill Climbing Optimization:")
    optimal_solution = hill_climbing(initial_guess, step_size, max_iterations)

    print(f"\nThe optimal solution is: x = {optimal_solution}")
    print(f"The maximum value of the objective function is: {objective_function(optimal_solution)}")

if __name__ == "__main__":
    main()
