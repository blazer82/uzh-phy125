"""
    Using the code of exercise 4b to plot the solar system
"""

import numpy as np
import matplotlib.pyplot as plt
from math import pi
from exercise4b import kepler, kepler_prime, coordinate, find_root


if __name__ == '__main__':

    planets = [
        { "name": "Mercury", "a": 0.387, "e": 0.2056 },
        { "name": "Venus", "a": 0.723, "e": 0.0067 },
        { "name": "Earth", "a": 1, "e": 0.0167 },
        { "name": "Mars", "a": 1.524, "e": 0.0935 },
        { "name": "Jupiter", "a": 5.203, "e": 0.0484 },
        { "name": "Saturn", "a": 9.5826, "e": 0.0565 },
        { "name": "Uranus", "a": 19.201, "e": 0.0472 },
        { "name": "Neptun", "a": 30.070, "e": 0.0086 },
        { "name": "Halley", "a": 17.8, "e": 0.967, "style": "." },
    ]

    # Plot results
    plt.title("Solar System")
    plt.xlabel("AU")
    plt.ylabel("AU")

    for planet in planets:
        nbr_of_steps = 400

        M_space = np.linspace(0, 2 * pi, nbr_of_steps)

        x = []
        y = []
        for M in M_space:
            def local_kepler(E):
                return kepler(E, planet["e"], M)

            def local_kepler_prime(E):
                return kepler_prime(E, planet["e"])

            # Find E
            E = find_root(local_kepler, local_kepler_prime)

            # Calculate coordinates
            (x_i, y_i) = coordinate(planet["e"], E, planet["a"])
            x.append(x_i)
            y.append(y_i)


        if "style" in planet:
            plt.plot(x, y, planet["style"], label=planet["name"])
        else:
            plt.plot(x, y, '-', label=planet["name"])

    plt.plot([0], [0], '.', label="Sun") # Plot the sun (0,0) (approximately) for reference
    plt.axis("equal")
    plt.legend(loc="best")
    # plt.savefig('solar_system.pdf')
    plt.show()
