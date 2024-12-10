import numpy as np
import matplotlib.pyplot as plt
from lab01.functions import launch_angle_range  # Correct import
import os  # Import os module for directory handling

def main():
    ve_v0 = 2.0  # Constant velocity ratio
    tol_alpha = 0.04  # Tolerance for altitude
    alpha_values = np.linspace(0.01, 0.5, 100)  # Range of alpha values

    min_angles = []
    max_angles = []

    for alpha in alpha_values:
        try:
            print(f"Calculating for alpha = {alpha}")
            phi_range = launch_angle_range(ve_v0, alpha, tol_alpha)
            min_angles.append(phi_range[0])
            max_angles.append(phi_range[1])
        except ValueError as e:
            print(f"Error for alpha={alpha}: {e}")
            min_angles.append(np.nan)  # Append NaN for invalid angles
            max_angles.append(np.nan)  # Append NaN for invalid angles

    # Ensure figures directory exists
    if not os.path.exists('figures'):
        os.makedirs('figures')

    # Plot results
    plt.plot(alpha_values, min_angles, label='Min Launch Angle', color='blue')
    plt.plot(alpha_values, max_angles, label='Max Launch Angle', color='red')

    plt.xlabel('Alpha (Fraction of Earth\'s Radius)')
    plt.ylabel('Launch Angle (Radians)')
    plt.title('Launch Angle vs Alpha for ve/v0 = 2.0')
    plt.legend()
    plt.savefig('figures/launch_angle_vs_alpha.png')  # Save plot in figures directory
    plt.show()

if __name__ == "__main__":
    main()
