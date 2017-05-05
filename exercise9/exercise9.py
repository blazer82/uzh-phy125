"""
    Exercise 9: Numerische Integration
"""

import numpy as np


def rectangle_method(a, b, func, N=10):
    # Slice width
    h = (b - a) / N

    # Discrete x values
    x = np.linspace(a, b, N+1)

    result = 0
    for i in range(N):
        y = (func(x[i]) + func(x[i+1])) / 2
        result += h*y
    return result


if __name__ == '__main__':

    a = 0
    b = 2
    f = np.cos
    F = np.sin
    result = F(b) - F(a)

    slices = 10

    rect_result = rectangle_method(a, b, f, slices)
    rect_error = rect_result - result
    print("\nRectangle method ({slices} slices): {result} (error {error})".format(result=rect_result, error=rect_error, slices=slices))

    print("\n")
