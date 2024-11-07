import math

def f(t_i, w_i):
    # Define the function f(t, y)
    return t_i + w_i

def predictor_formula(stepSize):
    # Initial values
    t_0, t_1, t_2, t_3 = 0, 0.2, 0.4, 0.6
    w_0, w_1, w_2, w_3 = 0.95, 0.68, 0.55, 0.3

    return w_3 + (stepSize / 24.0) * (55 * f(t_3, w_3) - 59 * f(t_2, w_2) + 37 * f(t_1, w_1) - 9 * f(t_0, w_0))

def corrector_formula(stepSize):
    # Initial values
    t_0, t_1, t_2, t_3 = 0, 0.2, 0.4, 0.6
    w_0, w_1, w_2, w_3 = 0.95, 0.68, 0.55, 0.3

    return w_3 + (stepSize / 24.0) * (9 * predictor_formula(0.2) + 19 * f(t_3, w_3) - 5 * f(t_2, w_2) + f(t_1, w_1))

# Print the results of the predictor and corrector formulas
print(predictor_formula(0.2))
print(corrector_formula(0.2))
