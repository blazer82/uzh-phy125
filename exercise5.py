"""
    Exercise 5: Galton, Pascal, Gauss
"""

import numpy as np
import matplotlib.pyplot as plt

def galton(balls, layers=5):
    """
    Implementation of Galton board

    Arguments
    ---------
    balls: int, Number of balls (simulation runs)
    layers: int, Number of layers on the board

    Return
    ------
    numpy array, Array of positions after each run
    """
    positions = []
    for b in range(balls):
        path = np.random.choice([0, 1], layers)
        positions.append(np.sum(path))
    return np.array(positions)

def pascal(layers=5):
    """
    Implementation of Pascal triangle

    Arguments
    ---------
    layers: int, Number of layers in the triangle

    Return
    ------
    numpy array, Array containing the final layer
    """

    prev_layer = np.array([1])
    for l in range(1, layers + 1):
        layer = np.zeros(l+1)
        layer[:-1] += prev_layer
        layer[1:] += prev_layer
        prev_layer = layer
    return layer


if __name__ == '__main__':

    # Set layers for all simulations
    layers = 10
    x = np.array(range(layers + 1))

    # Simulate Galton board
    balls = 1000
    galton_result = galton(balls, layers)
    galton_y = np.array([np.sum(galton_result == i) for i in x]) / balls

    # Build Pascal triangle
    pascal_result = pascal(layers)
    pascal_y = pascal_result / (2**layers)

    # Plot results
    plt.title("Galton, Pascal")
    plt.xlabel("Position")
    plt.ylabel("Probability")
    plt.bar(x-0.2, galton_y, width=0.4, label="Galton")
    plt.bar(x+0.2, pascal_y, width=0.4, label="Pascal")
    plt.legend(loc="best")
    plt.show()
