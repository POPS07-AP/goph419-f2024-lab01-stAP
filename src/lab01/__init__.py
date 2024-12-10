import numpy as np


def arcsin(x):
    """Compute arcsin using Borwein & Chamberland's approximation."""
    sum_result = x  # Start with x for the series
    term = x  # Initialize the first term of the series
    for n in range(1, 20):  # Series expansion for 20 terms
        term *= (2 * n - 1) ** 2 * x ** 2 / (2 * n * (2 * n + 1))
        sum_result += term
    return sum_result


def launch_angle(ve_v0, alpha):
    """Compute the launch angle using Eq. (17)."""
    x = np.sqrt(1 - (ve_v0 ** 2 * (1 - 1 / (1 + alpha)))) / ve_v0
    return arcsin(x)


def launch_angle_range(ve_v0, alpha, tol_alpha):
    """Compute minimum and maximum allowable launch angles."""
    alpha_min = (1 - tol_alpha) * alpha
    alpha_max = (1 + tol_alpha) * alpha

    min_angle = launch_angle(ve_v0, alpha_min)
    max_angle = launch_angle(ve_v0, alpha_max)

    return np.array([min_angle, max_angle])


# Example test
ve_v0 = 2.0
alpha = 0.25
tol_alpha = 0.02
phi_range = launch_angle_range(ve_v0, alpha, tol_alpha)
print("Launch angle range:", phi_range)
