import math

# Define f_t_y, which is the first-order differential y'
def f_t_y(t_i, w_i):
    return t_i * math.exp(3 * t_i) - 2 * w_i

# Main function implementing the Runge-Kutta 2nd order method (RK2)
def runge_kutta_2(stepSize, iterations):
    t_0 = 0
    w_0 = 0
    iter_count = 1

    while iter_count <= iterations:
        # Calculate k1 and k2
        k_1 = stepSize * f_t_y(t_0, w_0)
        k_2 = stepSize * f_t_y(t_0 + stepSize, w_0 + k_1)

        # Compute next w value using the RK2 method
        nextWValue = w_0 + 0.5 * (k_1 + k_2)

        print(nextWValue)  # Print the next w value

        # Update t_0 for the next iteration
        t_0 = t_0 + stepSize
        w_0 = nextWValue
        iter_count += 1

# Initialize values and call the runge_kutta_2 function
stepSize = 0.5
iterations = 2
runge_kutta_2(stepSize, iterations)
