import numpy as np

def df(f, p, k, h=1e-5):
    """
    Computes the partial derivative of the function f with respect to the k-th component of the vector p.
    """
    p1 = p.copy()
    p1[k] = p[k] + h
    return (f(p1) - f(p)) / h

def grad(f, p):
    """
    Computes the gradient of the function f at the point p.
    """
    return np.array([df(f, p, k) for k in range(len(p))])

def gradient_descent(f, initial_point, learning_rate=0.01, tolerance=1e-6, max_iterations=1000):
    """
    Implements the gradient descent algorithm to find the minimum of the function f.
    """
    p = initial_point
    iterations = 0

    while iterations < max_iterations:
        f_now = f(p)
        gradient = grad(f, p)
        p = p - learning_rate * gradient

        f_next = f(p)

        if np.abs(f_now - f_next) < tolerance:
            print("Converged to the minimum.")
            break

        iterations += 1
        print(f"Iteration {iterations}: p = {p}, f(p) = {f_next}")

    return p

# Example function: f(p) = p[0]^2 + p[1]^2 + p[2]^2
def example_function(p):
    return np.sum(p**2)

# Initial guess for the minimum
initial_point = np.array([2.0, 1.0, 3.0])

# Run gradient descent on the example function
result = gradient_descent(example_function, initial_point)

print("\nOptimal solution:", result)
print("Minimum value of the objective function:", example_function(result))
