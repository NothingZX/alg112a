def quadratic_function(x):
    return x**2 - 3*x + 1

def derivative_quadratic_function(x):
    return 2*x - 3

def solve_quadratic_equation_iteratively(initial_guess, tolerance=1e-6, max_iterations=100):
    x_current = initial_guess

    for iteration in range(max_iterations):
        f_x_current = quadratic_function(x_current)
        f_prime_x_current = derivative_quadratic_function(x_current)

        if abs(f_x_current) < tolerance:
            # The solution is within the tolerance
            return x_current

        # Update the guess using the Newton-Raphson formula
        x_next = x_current - f_x_current / f_prime_x_current
        x_current = x_next

    # If the maximum number of iterations is reached, return None (indicating no convergence)
    return None

def main():
    # Example: Solve x^2 - 3x + 1 = 0 iteratively
    initial_guess = 0.0
    solution = solve_quadratic_equation_iteratively(initial_guess)

    if solution is not None:
        print(f"The solution is: x = {solution}")
    else:
        print("The iterative method did not converge within the specified iterations.")

if __name__ == "__main__":
    main()
