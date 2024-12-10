import numpy as np




import numpy as np


def arcsin(x):
    """Compute arcsin using the Taylor series expansion."""
    if x < -1 or x > 1:
        raise ValueError("Input for arcsin must be between -1 and 1.")

    sum_result = x  # Start with the first term in the Taylor series
    term = x  # Initialize the first term
    for n in range(1, 20):  # Using 20 terms for precision
        term *= (2 * n - 1) ** 2 * x ** 2 / (2 * n * (2 * n + 1))
        sum_result += term
    return sum_result


def launch_angle(ve_v0, alpha):
    """Compute the launch angle using Equation (17)."""

    # Calculate the square root term (must be non-negative)
    term_inside_sqrt = 1 - (ve_v0 ** 2 * (1 - 1 / (1 + alpha)))

    # Check if the term inside the square root is negative
    if term_inside_sqrt < 0:
        raise ValueError(f"Invalid input: square root term is negative for ve/v0={ve_v0} and alpha={alpha}.")

    # Calculate the right-hand side (x value) of Equation (17)
    x = np.sqrt(term_inside_sqrt) / ve_v0

    # Calculate and return the launch angle using the arcsin function
    return arcsin(x)


def launch_angle_range(ve_v0, alpha, tol_alpha):
    """Compute the minimum and maximum allowable launch angles."""
    alpha_min = (1 - tol_alpha) * alpha
    alpha_max = (1 + tol_alpha) * alpha

    min_angle = launch_angle(ve_v0, alpha_min)
    max_angle = launch_angle(ve_v0, alpha_max)

    return np.array([min_angle, max_angle])