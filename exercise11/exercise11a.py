"""
    Exercise 11: Chaos Pendel
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


if __name__ == "__main__":

    b = 2  # Inner leg
    l = 3  # Outer leg
    omega = 1  # Angular velocity
    epsilon = b / l * omega**2

    def Q(q, t):
        return (q[1], -np.sin(q[0]) - epsilon * np.sin(q[0] - omega * t))

    def inner_leg(t):
        return (b * np.sin(omega * t), b * -np.cos(omega * t))

    def outer_leg(q, X, Y):
        return (X + l * np.sin(q), Y - l * np.cos(q))

    # Solve differential equation
    t = np.linspace(0, 100, 1000)
    q = odeint(Q, [0, 1], t)[:,1]

    # Calculate inner leg
    (X_i, Y_i) = inner_leg(t)

    # Calculate outer leg
    (X_o, Y_o) = outer_leg(q, X_i, Y_i)

    # Plot
    plt.plot(X_i, Y_i)
    plt.plot(X_o, Y_o)
    plt.axes().set_aspect('equal')
    plt.axis(np.array([-1, 1, -1, 1]) * (b + l) * 1.5)
    plt.show()
