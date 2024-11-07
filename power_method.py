import numpy as np

def power_method(A, x, max_iterations=20):
    """
    Power Method to approximate the dominant eigenvalue and eigenvector of matrix A.
    
    Parameters:
    - A: n x n matrix (numpy array)
    - x: Initial non-zero vector (numpy array)
    - max_iterations: Number of iterations to run
    
    Returns:
    - eigenvalue: Approximated dominant eigenvalue after 5 iterations
    - eigenvector: Approximated eigenvector (normalized)
    """
    # Ensure x is a non-zero vector and has the correct dimensions
    n = A.shape[0]
    x = x / np.linalg.norm(x)  # Normalize the initial vector

    for k in range(max_iterations):
        # Step 5: Set y = Ax
        y = np.dot(A, x)
        
        # Step 6: Compute the Rayleigh quotient to approximate the eigenvalue
        eigenvalue = np.dot(x.T, y)
        
        # Step 7: Normalize the vector y
        y_norm = np.linalg.norm(y)
        if y_norm == 0:
            print("A has the eigenvalue 0, select a new vector x and restart.")
            return None, None
        
        # Step 8: Normalize the vector
        x_new = y / y_norm
        
        # Step 9: Update x
        x = x_new

    return eigenvalue, x

# Example usage:

# Define the matrix A (example 3x3 matrix)
A = np.array([[4, 1, 2],
              [1, 3, 0],
              [2, 0, 5]])

# Initial vector x (random or chosen non-zero vector)
x = np.array([1, 1, 1])

# Call the power method function for 5 iterations
eigenvalue, eigenvector = power_method(A, x, max_iterations=5)

if eigenvalue is not None:
    print(f"Dominant Eigenvalue (after 5 iterations): {eigenvalue}")
    print(f"Associated Eigenvector (after 5 iterations): {eigenvector}")
