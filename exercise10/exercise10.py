"""
    Exercise 10: Integrationsmethoden für ODE's
"""

import numpy as np
import matplotlib.pyplot as pl


def euler(func, init, time):
    y = []
    x_old = init
    len_i = np.max(time) / (len(time) - 1)
    y.append(init)
    for i in time[1:]:
        x_new = x_old + func(x_old, i) * len_i
        y.append(x_new)
        x_old = x_new
    return y


def runge_kutta(func, init, time):
    y = []
    x_old = init
    len_i = np.max(time) / (len(time) - 1)
    y.append(init)
    for i in time[1:]:
        f_x = func(x_old, i)
        x_new = x_old + len_i * (f_x + func(x_old + len_i * f_x, i)) / 2
        y.append(x_new)
        x_old = x_new
    return y

def F(X, t):
    return np. array([X[2], X[3], 0, -1])


def G(X, t, w=2.28):
    return np.array([X[2], X[3], 2*X[3], -2*X[2] + np.cos(w*t)])


if __name__ == "__main__":

    # Exercise 1

    ini = np.array([0, 0, 1, 5])
    t = np.linspace(0, 10, 21)
    pl.plot(t, t * (5 - t / 2), label='Truth')

    pos = euler(F, ini, t)
    yarray = [y[1] for y in pos]
    pl.plot(t, yarray, '+', label='Euler')

    pos = runge_kutta(F, ini, t)
    yarray = [y[1] for y in pos]
    pl.plot(t, yarray, '+', label='Runge Kutta')

    pl. axes().set_aspect('equal')
    pl.legend()
    pl.show()

    # Exercise 2

    w = 2.28
    frac = 1 / (4 - w**2)
    ini = np.array([0, 1 + frac, 2 + 2 * frac, 0])
    t = np.linspace(0, 10, 21)

    x_t = np.sin(2*t) + 2*np.sin(w*t) * frac / w
    y_t = 2*np.cos(2*t) + ((2*np.cos(w*t)*w)*(w*(4-w**2)))/(2*w**2*(4-w**2)**2)
    pl.plot(x_t, y_t, label='Truth')

    pos = runge_kutta(G, ini, t)
    xarray = [x[0] for x in pos]
    yarray = [y[1] for y in pos]
    pl.plot(xarray, yarray, label='Zyklotron')

    pl.legend()
    pl.axes().set_aspect('equal')
    pl.show()
