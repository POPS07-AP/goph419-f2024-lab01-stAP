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


import numpy as np
import matplotlib.pyplot as plt
from lab01.functions import launch_angle_range


def main():
    ve_v0 = 2.0
    tol_alpha = 0.04
    alpha_values = np.linspace(0.01, 0.5, 100)

    min_angles = []
    max_angles = []

    for alpha in alpha_values:
        phi_range = launch_angle_range(ve_v0, alpha, tol_alpha)
        min_angles.append(phi_range[0])
        max_angles.append(phi_range[1])

    plt.plot(alpha_values, min_angles, label='Min Launch Angle', color='b')
    plt.plot(alpha_values, max_angles, label='Max Launch Angle', color='r')

    plt.xlabel('Alpha (Fraction of Earth\'s Radius)')
    plt.ylabel('Launch Angle (Radians)')
    plt.title('Launch Angle vs Alpha for ve/v0 = 2.0')
    plt.legend()
    plt.savefig('figures/plot_example.png')
    plt.show()


if __name__ == "__main__":
    main()


def plot_ve_v0_range():
    alpha = 0.25
    tol_alpha = 0.04
    ve_v0_values = np.linspace(1.0, 3.0, 100)

    min_angles = []
    max_angles = []

    for ve_v0 in ve_v0_values:
        phi_range = launch_angle_range(ve_v0, alpha, tol_alpha)
        min_angles.append(phi_range[0])
        max_angles.append(phi_range[1])

    plt.plot(ve_v0_values, min_angles, label='Min Launch Angle', color='blue')
    plt.plot(ve_v0_values, max_angles, label='Max Launch Angle', color='red')

    plt.xlabel('ve/v0 (Escape Velocity to Terminal Velocity Ratio)')
    plt.ylabel('Launch Angle (Radians)')
    plt.title('Launch Angle vs ve/v0 for alpha = 0.25')
    plt.legend()
    plt.savefig('figures/plot_example.png')
    plt.show()


if __name__ == "__main__":
    plot_ve_v0_range()

