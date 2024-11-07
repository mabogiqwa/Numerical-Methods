import numpy as np
import math

def linear_finite_difference(p_x, q_x, r_x, a, b, alpha, beta, n):
    h = (b - a) / (n + 1)
    h = 0.05

    # Initialize arrays
    x = np.linspace(a, b, n + 2)
    a_i = np.zeros(n + 1)
    b_i = np.zeros(n + 1)
    c_i = np.zeros(n + 1)
    d_i = np.zeros(n + 1)
    l_i = np.zeros(n + 1)
    u_i = np.zeros(n + 1)
    z_i = np.zeros(n + 1)
    w_i = np.zeros(n + 2)

    # Calculate coefficients
    for i in range(1, n):
        x_i = a + i * h
        a_i[i] = 2 + h**2 * q_x(x_i)
        b_i[i] = -1 + (h / 2) * p_x(x_i)
        c_i[i] = -1 - (h / 2) * p_x(x_i)
        d_i[i] = -h**2 * r_x(x_i)

    # Handle boundary conditions
    a_i[0] = 2 + h**2 * q_x(x[1])
    b_i[0] = -1 + (h / 2) * p_x(x[1])
    d_i[0] = -h**2 * r_x(x[1]) + (1 + (h / 2) * p_x(x[1])) * alpha

    a_i[n] = 2 + h**2 * q_x(x[n])
    c_i[n] = -1 - (h / 2) * p_x(x[n])
    d_i[n] = -h**2 * r_x(x[n]) + (1 - (h / 2) * p_x(x[n])) * beta

    # Solve tridiagonal system
    l_i[1] = a_i[1]
    u_i[1] = b_i[1] / a_i[1]
    z_i[1] = d_i[1] / l_i[1]

    for i in range(2, n + 1):
        l_i[i] = a_i[i] - c_i[i] * u_i[i - 1]
        u_i[i] = b_i[i] / l_i[i]
        z_i[i] = (d_i[i] - c_i[i] * z_i[i - 1]) / l_i[i]

    # Back-substitution
    w_i[n] = z_i[n]
    for i in range(n - 1, 0, -1):
        w_i[i] = z_i[i] - u_i[i] * w_i[i + 1]

    w_i[0] = alpha
    w_i[n + 1] = beta

    return x, w_i

# Define the functions p(x), q(x), and r(x) for your specific problem
def p_x(x):
    # Replace this with the actual function for p(x)
    return 0

def q_x(x):
    # Replace this with the actual function for q(x)
    return 100

def r_x(x):
    # Replace this with the actual function for r(x)
    return 0

# Set the boundary conditions and interval
a = 0
b = 1
alpha = 1
beta = math.exp(-0.01)
n = 10  # Number of subintervals

# Calculate the solution
x, w = linear_finite_difference(p_x, q_x, r_x, a, b, alpha, beta, n)

# Print the results
print("x values:\n", np.array(x))
print("\nw values:\n", np.array(w))