"""
    Exercise 5: Galton, Pascal, Gauss
"""

import numpy as np
import matplotlib.pyplot as plt

def galton(balls, layers):
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

def pascal(layers):
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

def gauss(x, N, mean, std_dev):
    """
    Implementation of central limit theorem using a Gaussian function

    Arguments
    ---------
    x: float
    N: int
    mean: float, Mean
    std_dev: float, Standard deviation

    Return
    ------
    float
    """
    return np.exp(-(x-N*mean)**2/(2*N*std_dev**2)) / (np.sqrt(N)*std_dev) / np.sqrt(2*np.pi)


if __name__ == '__main__':

    # Set layers for all simulations
    layers = 10
    x = np.array(range(layers + 1))

    # Simulate Galton board
    balls = 10000
    galton_result = galton(balls, layers)
    galton_y = np.array([np.sum(galton_result == i) for i in x]) / balls

    # Calculate Gauss distribution
    gauss_x = np.linspace(0, layers, 1000)
    gauss_y = [gauss(x, layers, 0.5, 0.5) for x in gauss_x]

    # Build Pascal triangle
    pascal_result = pascal(layers)
    pascal_y = pascal_result / (2**layers)

    # Plot results
    plt.subplot(2, 1, 1)
    plt.title("Galton, Pascal, Gauss")
    plt.ylabel("P(x)")
    plt.bar(x-0.2, galton_y, width=0.4, label="Galton")
    plt.bar(x+0.2, pascal_y, width=0.4, label="Pascal")
    plt.legend(loc="best")

    plt.subplot(2, 1, 2)
    plt.xlabel("Bin")
    plt.ylabel("P(x)")
    plt.plot(gauss_x, gauss_y, label="Gauss")
    plt.legend(loc="best")

    plt.savefig('galton_pascal_gauss.pdf')
    plt.show()
