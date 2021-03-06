"""
    Exercise 9: Numerische Integration
"""

import numpy as np


def rectangle_method(a, b, func, N=10):
    """
    Implementation of the rectangle method to integrate

    Arguments
    ---------
    a: float, Lower boundary
    b: floar, Upper boundary
    func: function, Function to integrate
    N: int, amount of slices to use

    Return
    ------
    float, Integration result
    """

    # Slice width
    h = (b - a) / N

    # Discrete x values
    x = np.linspace(a, b, N+1)

    result = 0
    for i in range(N):
        y = (func(x[i]) + func(x[i+1])) / 2
        result += h*y
    return result

def simpson(a, b, func, N=10):
    """
    Implementation of the Simpson method to integrate

    Arguments
    ---------
    a: float, Lower boundary
    b: floar, Upper boundary
    func: function, Function to integrate
    N: int, amount of slices to use

    Return
    ------
    float, Integration result
    """

    def single_simpson(a, b, func):
        """
        Single simpson interpolation
        """
        return ((b - a) * func(a) / 6) + (2 * (b - a) * func((a + b) / 2) / 3) + ((b - a) * func(b) / 6)

    # Discrete x values
    x = np.linspace(a, b, N+1)

    result = 0
    for i in range(N):
        result += single_simpson(x[i], x[i+1], func)
    return result


if __name__ == '__main__':

    a = 0  # Lower boundary
    b = 2  # Upper boundary
    f = np.cos  # Function to integrate
    F = np.sin  # Antiderivative
    result = F(b) - F(a)  # Correct result

    # Amount of slices to use
    slices = 10

    # Rectangle method (exercise 1)
    rect_result = rectangle_method(a, b, f, slices)
    rect_error = rect_result - result
    print("\nRectangle method ({slices} slices): {result} (error {error})".format(result=rect_result, error=rect_error, slices=slices))

    # Simpson method (exercise 2)
    simpson_result = simpson(a, b, f, slices)
    simpson_error = simpson_result - result
    print("\nSimpson method ({slices} slices): {result} (error {error})".format(result=simpson_result, error=simpson_error, slices=slices))

    print("\n")
