"""
    Exercise 4b: Show me your planets

    Plot of comet Halley's orbit around the sun
"""

import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, sqrt, pi

# Define kepler function
def kepler(E, e, M):
    return E - e * sin(E) + M

# Define first derivative of kepler function
def kepler_prime(E, e):
    return 1 - e * cos(E)

# Define coordinate function
def coordinate(e, E, a):
    return (a * (cos(E) - e), a * (sqrt(1 - e**2) * sin(E)))

# Define function to find root of functions
def find_root(func, func_prime, x=1):
    iterations = []
    while not x in iterations:
        iterations.append(x)
        x = x - func(x)/func_prime(x)
    return x


if __name__ == '__main__':

    a = 17.8 # Semi-major axis
    e = 0.967 # Eccentricity

    nbr_of_steps = 100

    M_space = np.linspace(0, 2 * pi, nbr_of_steps, endpoint=False)

    x = []
    y = []
    for M in M_space:
        def local_kepler(E):
            return kepler(E, e, M)

        def local_kepler_prime(E):
            return kepler_prime(E, e)

        # Find E
        E = find_root(local_kepler, local_kepler_prime)

        # Calculate coordinates
        (x_i, y_i) = coordinate(e, E, a)
        x.append(x_i)
        y.append(y_i)

    # Plot results
    plt.title("Comet Halley's Orbit")
    plt.xlabel("AU")
    plt.ylabel("AU")
    plt.plot(x, y, '.')
    plt.plot([0], [0], '.') # Plot the sun (0,0) (approximately) for reference
    plt.axis('equal')
    plt.savefig('comet_halley.pdf')
    plt.show()
