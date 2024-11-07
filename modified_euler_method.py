import math

# Define f_t_y, which is the first-order differential y'
def f_t_y(t_i, w_i):
    return t_i * math.exp(3 * t_i) - 2 * w_i

# Main function that implements the modified Euler method
def modified_euler_method(stepSize, iterations):
    w_0 = 0
    t_0 = 0
    
    iter_count = 1
    while iter_count <= iterations:
        # Calculate the next t and w values
        nextTValue = t_0 + stepSize

        nextWValue = w_0 + (stepSize / 2) * (f_t_y(t_0, w_0) + f_t_y(nextTValue, w_0 + stepSize * f_t_y(t_0, w_0)))
        
        print(nextWValue)  # Print the next w value
        t_0 = nextTValue
        print(t_0)  # Print the next t value
        w_0 = nextWValue

        iter_count += 1

# Initialize values and call the modified Euler method
stepSize = 0.5
iterations = 2
modified_euler_method(stepSize, iterations)
