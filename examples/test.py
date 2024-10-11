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