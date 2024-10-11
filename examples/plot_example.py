import matplotlib.pyplot as plt
import numpy as np

from lab01.functions import arcsin

def main():
    x = np.linspace(-0.95, 0.95, 100)
    y = np.array([arcsin(x) for x in x])
    plt.plot(x, y, "-b", label="arcsin")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.savefig("figures/plot_example.png")

if __name__ == "__main__":
    main()
