import numpy as np
import math

# Define the function F(x, y, y') based on the problem
def F(x, y, yp):
    return -(yp)**2 - y + math.log(x)

# Define the partial derivatives of F with respect to y and y'
def FY(x, y, yp):
    return -1  # Partial derivative of F with respect to y

def FYP(x, y, yp):
    return -2 * yp  # Partial derivative of F with respect to y'

# Nonlinear finite-difference method
def nonlinear_fd_method(F, FY, FYP, A, B, ALPHA, BETA, N, TOL, NN):
    # Step 1: Calculate step size
    H = (B - A) / (N + 1)
    
    # Step 2: Initialize W
    W = np.zeros(N)  # Array to hold values of y
    for i in range(1, N + 1):
        W[i - 1] = ALPHA + i * H * (BETA - ALPHA) / (B - A)

    # Step 3: Start iteration
    K = 1
    OK = True
    
    while K <= NN and OK:
        # Step 4: Solve for A, B, and D2
        X = A + H
        T = (W[0] - ALPHA) / (2 * H)
        A_arr = np.zeros(N)
        B_arr = np.zeros(N)
        C_arr = np.zeros(N)
        D2_arr = np.zeros(N)
        
        A_arr[0] = 2 + H**2 * FY(X, W[0], T)
        B_arr[0] = -1 + H * FYP(X, W[0], T) / 2
        D2_arr[0] = -(2 * W[0] - W[1] - ALPHA + H**2 * F(X, W[0], T))

        # Fill the A, B, C, D2 arrays for all interior points
        for i in range(1, N - 1):
            X = A + (i + 1) * H
            T = (W[i] - W[i - 1]) / (2 * H)
            A_arr[i] = 2 + H**2 * FY(X, W[i], T)
            B_arr[i] = -1 + H * FYP(X, W[i], T) / 2
            C_arr[i] = -1 - H * FYP(X, W[i], T) / 2
            D2_arr[i] = -(2 * W[i] - W[i + 1] - W[i - 1] + H**2 * F(X, W[i], T))
        
        # Boundary condition at the right endpoint
        X = B - H
        T = (BETA - W[N - 2]) / (2 * H)
        A_arr[N - 1] = 2 + H**2 * FY(X, W[N - 1], T)
        C_arr[N - 1] = -1 - H * FYP(X, W[N - 1], T) / 2
        D2_arr[N - 1] = -(2 * W[N - 1] - W[N - 2] - BETA + H**2 * F(X, W[N - 1], T))

        # Step 5: Solve the tridiagonal system (LU Decomposition)
        L = np.zeros(N)
        U = np.zeros(N)
        Z = np.zeros(N)

        # Forward substitution
        L[0] = A_arr[0]
        U[0] = B_arr[0] / A_arr[0]
        Z[0] = D2_arr[0] / L[0]
        
        for i in range(1, N - 1):
            L[i] = A_arr[i] - C_arr[i] * U[i - 1]
            U[i] = B_arr[i] / L[i]
            Z[i] = (D2_arr[i] - C_arr[i] * Z[i - 1]) / L[i]

        L[N - 1] = A_arr[N - 1] - C_arr[N - 1] * U[N - 2]
        Z[N - 1] = (D2_arr[N - 1] - C_arr[N - 1] * Z[N - 2]) / L[N - 1]

        # Back substitution
        V = np.zeros(N)
        V[N - 1] = Z[N - 1]
        VMAX = abs(V[N - 1])
        W[N - 1] = W[N - 1] + V[N - 1]

        for i in range(N - 2, -1, -1):
            V[i] = Z[i] - U[i] * V[i + 1]
            W[i] = W[i] + V[i]
            if abs(V[i]) > VMAX:
                VMAX = abs(V[i])
        
        # Step 6: Check for convergence
        if VMAX <= TOL:
            print(f"Convergence in {K} iterations")
            break
        else:
            K += 1

        if K > NN:
            print(f"No convergence in {NN} iterations")

    return W

# Parameters for the problem
A = 1  # Left endpoint
B = 2  # Right endpoint
ALPHA = 0  # Boundary condition at A
BETA = math.log(2)  # Boundary condition at B
N = 10  # Number of subintervals
TOL = 1e-6  # Tolerance
NN = 100  # Maximum number of iterations

# Call the nonlinear finite-difference method
W = nonlinear_fd_method(F, FY, FYP, A, B, ALPHA, BETA, N, TOL, NN)

# Output the results
print("Results:")
for i in range(N):
    x = A + (i + 1) * (B - A) / (N + 1)
    print(f"X = {x:.8f}, Y(X) = {W[i]:.8f}")
