import numpy as np

def poisson_finite_difference(f, g, a, b, c, d, N, M, max_iter, tol):
    """
    Solves the Poisson equation using the finite difference method.

    Args:
        f: The right-hand side function f(x, y).
        g: The boundary condition function g(x, y).
        a, b: The x-interval [a, b].
        c, d: The y-interval [c, d].
        N: The number of grid points in the x-direction.
        M: The number of grid points in the y-direction.
        max_iter: The maximum number of iterations.
        tol: The tolerance for convergence.

    Returns:
        The solution to the Poisson equation.
    """

    # Initialize grid points and step sizes
    h = (b - a) / (N - 1)
    k = (d - c) / (M - 1)

    # Initialize solution matrix
    u = np.zeros((M, N))

    # Define the x and y grids
    x = np.linspace(a, b, N)
    y = np.linspace(c, d, M)

    # Apply boundary conditions
    for j in range(M):
        u[j, 0] = g(x[0], y[j])    # left boundary (x = a)
        u[j, -1] = g(x[-1], y[j])   # right boundary (x = b)
    for i in range(N):
        u[0, i] = g(x[i], y[0])     # bottom boundary (y = c)
        u[-1, i] = g(x[i], y[-1])   # top boundary (y = d)

    # Set lambda
    lam = 1 / (2 * ((1 / h**2) + (1 / k**2)))

    # Initialize u_old for convergence check
    u_old = u.copy()

    # Perform Gauss-Seidel iterations
    iter_count = 0
    while iter_count < max_iter:
        iter_count += 1
        for i in range(1, M - 1):
            for j in range(1, N - 1):
                u[i, j] = lam * ((u[i + 1, j] + u[i - 1, j]) / h**2 +
                                (u[i, j + 1] + u[i, j - 1]) / k**2 - f(x[j], y[i]))

        # Check for convergence
        if np.max(np.abs(u - u_old)) < tol:
            break
        u_old = u.copy()

    return u

# Define the functions f(x, y) and g(x, y) for the given problem
def f(x, y):
    return 4

def g(x, y):
    if y == 0:
        return x**2
    elif y == 2:
        return (x - 2)**2
    elif x == 0:
        return y**2
    else:
        return (y - 1)**2

# Set the parameters
a = 0
b = 1
c = 0
d = 2
N = 4  # Using h = 1/2
M = 5  # Using k = 1/2
max_iter = 1000
tol = 1e-6

# Calculate the solution
u = poisson_finite_difference(f, g, a, b, c, d, N, M, max_iter, tol)

# Print the solution
print(u)
