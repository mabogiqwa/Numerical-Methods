import math

# Define f_t_y, which is the first-order differential y'
def f_t_y(t_i, w_i):
    return t_i * math.exp(3 * t_i) - 2 * w_i

# Define f_t_y_derivative, the derivative of f(t, y), i.e., y''
def f_t_y_derivative(t_i, w_i):
    return math.exp(3 * t_i) + 3 * t_i * math.exp(3 * t_i) - 2 * (t_i * math.exp(3 * t_i) - 2 * w_i)

# Compute second-order Taylor expansion
def compute_second_order_taylor(t_i, w_i, stepSize):
    return f_t_y(t_i, w_i) + (stepSize / 2.0) * f_t_y_derivative(t_i, w_i)

# Compute the next w value using the Taylor series approximation
def compute_next_w_value(t_i, w_i, stepSize):
    w_0 = w_i
    iter_count = 0
    i = 0

    while iter_count < 3:
        print(f"The value of w_i is: {w_0}")
        next_w_value = w_0 + stepSize * compute_second_order_taylor(t_i, w_0, stepSize)

        w_0 = next_w_value
        t_i = t_i + stepSize  # Correcting how t_i is updated
        iter_count += 1  # Increment the iteration count for the loop

# Initialize values and call the function
t_0 = 0
w_0 = 0
stepSize = 0.5
compute_next_w_value(t_0, w_0, stepSize)

