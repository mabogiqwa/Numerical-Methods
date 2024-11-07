import math

# Define f_t_y, which is the first-order differential y'
def f_t_y(t_i, w_i):
    return 1/(t_i + w_i)

# Main function implementing the Runge-Kutta 4th order method (RK4)
def runge_kutta_4(stepSize, iterations):
    t_0 = 0
    w_0 = 2
    iter_count = 1

    while iter_count <= iterations:
        # Calculate k1, k2, k3, and k4
        k_1 = stepSize * f_t_y(t_0, w_0)
        k_2 = stepSize * f_t_y(t_0 + (stepSize / 2), w_0 + (k_1 / 2))
        k_3 = stepSize * f_t_y(t_0 + (stepSize / 2), w_0 + (k_2 / 2))
        k_4 = stepSize * f_t_y(t_0 + stepSize, w_0 + k_3)

        # Compute next w value based on iteration count
        nextWValue = w_0 + (1.0 / 6.0) * (k_1 + 2 * k_2 + 2 * k_3 + k_4)
        w_0 = nextWValue
        
        print('Iteration',iter_count,':')
        print('t_i: ',t_0,'w_i:',nextWValue)  # Print the next w value

        # Update t_0 for the next iteration
        t_0 = t_0 + stepSize
        iter_count += 1

# Initialize values and call the runge_kutta_4 function
stepSize = 0.2
iterations = 4
runge_kutta_4(stepSize, iterations)
