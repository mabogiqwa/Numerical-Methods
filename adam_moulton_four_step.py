import math

# Function to calculate f(t, y) for the differential equation
def get_output_of_d_function(t, y):
    return -3 * (t ** 2) * (y ** 2)

# Function to calculate the actual solution value for comparison
def get_output_of_solution_curve(t):
    return 2.0 / (2 * (t ** 3) + 1)

# Function to calculate the absolute error between approximate and actual values
def calculate_error(w_val, actual_val):
    return abs(actual_val - w_val)

# Main function to implement the modified Euler method
def main():
    val_of_lower_bound = -1.0  # Represents 'a' in [a, b]
    current_val_of_t = 0.0     # t_0
    current_val_of_w = 2.0     # w_0
    step_size = 0.2            # Step size h
    iterations = [
        "First iteration", "Second iteration", "Third iteration",
        "Fourth iteration", "Fifth iteration", "Sixth iteration"
    ]

    iter_count = 0
    while iter_count < 5:
        # Modified Euler Method Calculations
        temp_y_value1 = get_output_of_d_function(current_val_of_t, current_val_of_w)
        
        next_val_of_t = val_of_lower_bound + (step_size * (iter_count + 1))
        
        temp_y_value2 = current_val_of_w + (step_size * temp_y_value1)
        temp_y_value3 = get_output_of_d_function(next_val_of_t, temp_y_value2)
        
        next_val_of_w = current_val_of_w + (step_size * temp_y_value3)
        
        # Update values for the next iteration
        current_val_of_t = next_val_of_t
        current_val_of_w = next_val_of_w

        # Calculate the actual value and absolute error
        actual_value = get_output_of_solution_curve(current_val_of_t)
        absolute_error = calculate_error(current_val_of_w, actual_value)

        # Output results for the current iteration
        print(f"{iterations[iter_count]} where i is {iter_count + 1}:")
        print(f"Value of t_i: {current_val_of_t:.6f}")
        print(f"Value of w_i: {current_val_of_w:.6f}")
        print(f"Magnitude of error is: {absolute_error:.6f}\n")

        iter_count += 1

# Run the main function
if __name__ == "__main__":
    main()
