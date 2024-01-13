import numpy as np
import matplotlib.pyplot as plt

# Define a polynomial: P(x) = 3x^2 - 4x + 2
coefficients = [3, -4, 2]

# Create a numpy polynomial object
polynomial = np.poly1d(coefficients)

# Evaluate the polynomial at x = 2
result_at_x_2 = polynomial(2)
print(f"P(2) = {result_at_x_2}")

# Find roots of the polynomial (where P(x) = 0)
roots = np.roots(coefficients)
print(f"Roots of the polynomial: {roots}")

# Plot the polynomial
x_values = np.linspace(-3, 3, 100)
y_values = polynomial(x_values)

plt.plot(x_values, y_values, label="P(x) = 3x^2 - 4x + 2")
plt.scatter(roots, [0, 0], color='red', marker='o', label="Roots")
plt.xlabel("x")
plt.ylabel("P(x)")
plt.axhline(0, color='black', linewidth=0.5, linestyle="--")
plt.legend()
plt.show()
