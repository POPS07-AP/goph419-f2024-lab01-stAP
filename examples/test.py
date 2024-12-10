import numpy as np

from lab01.functions import arcsin

def test_arcsin():

    print("testing arcsin")

    x = 0
    expected = np.asin(x)
    actual = arcsin(x)
    print(f"x={x}, arcsin(x)={actual}, expected = {expected}")
    x = 0.5
    expected = np.asin(x)
    actual = arcsin(x)
    print(f"x={x}, arcsin(x)={actual}, expected = {expected}")
    x = -0.5
    expected = np.asin(x)
    actual = arcsin(x)
    print(f"x={x}, arcsin(x)={actual}, expected = {expected}")
    x = 0.95
    expected = np.asin(x)
    actual = arcsin(x)
    print(f"x={x}, arcsin(x)={actual}, expected = {expected}")
    x = 0.99
    expected = np.asin(x)
    actual = arcsin(x)
    print(f"x={x}, arcsin(x)={actual}, expected = {expected}")


if __name__ == "__main__":
    test_arcsin()

from lab01.functions import launch_angle_range
import numpy as np


def test_launch_angle_range():
    ve_v0 = 2.0
    alpha = 0.25
    tol_alpha = 0.02

    expected_min_angle = 0.219  # Example placeholder value
    expected_max_angle = 0.234  # Example placeholder value

    actual_angles = launch_angle_range(ve_v0, alpha, tol_alpha)
    min_angle, max_angle = actual_angles[0], actual_angles[1]

    assert np.isclose(min_angle, expected_min_angle, atol=1e-5), f"Min angle mismatch!"
    assert np.isclose(max_angle, expected_max_angle, atol=1e-5), f"Max angle mismatch!"
    print("Test passed!")


def test_invalid_input():
    try:
        launch_angle_range(0.5, 10, 0.02)  # Expected to raise error
    except ValueError as e:
        print(f"Test passed with error: {e}")


if __name__ == "__main__":
    test_launch_angle_range()
    test_invalid_input()
