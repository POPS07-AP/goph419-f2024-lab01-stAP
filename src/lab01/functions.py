import numpy as np


def arcsin(x):
    """Compute inverse sin(x)

    Parameters
    ----------
    x : float
        The argument of arcsin

    Returns
    -------
    float
    """
    sgn = 1 if x >= 0 else -1
    x = np.abs(x)
    result = 0.0
    eps_a = 1.0
    tol = 1.0e-16
    k = 1
    fact_k = 1
    fact_2k = 2
    k_max = 100
    while eps_a > tol and k < k_max:
        dy = (2*x) ** (2*k) / (k**2 * fact_2k/fact_k**2)
        result += dy
        eps_a = np.abs(dy / result)
        k += 1
        fact_k *= k
        fact_2k *= (2*k)*(2*k-1)
    return sgn*np.sqrt(0.5*result)