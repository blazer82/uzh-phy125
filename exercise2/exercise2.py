"""
    Excercise 2: Bernoulli
"""

from fractions import Fraction

def fibonacci(n):
    """
    Calculate n-th Fibonacci number

    Arguments
    ---------
    n: int

    Return
    ------
    int, n-th Fibonacci number
    """
    if n < 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def factorial(x):
    """
    Calculate factorial

    Arguments
    ---------
    x: int

    Return
    ------
    int, calculated factorial of x
    """
    if x < 1:
        return 1
    return factorial(x-1) * x

def bernoulli(n):
    """
    Calculate n-th Bernoulli number

    Arguments
    ---------
    n: int

    Return
    ------
    Fraction, n-th Bernoulli number
    """
    if n < 1:
        return Fraction(1, 1)
    b_sum = Fraction(0, 1)
    n_factorial = factorial(n)
    for k in range(n):
        b_sum += Fraction(n_factorial * bernoulli(k), factorial(k) * factorial(n-k+1))
    return -b_sum


if __name__ == '__main__':
    # Calculate fibonacci numbers
    for n in range(10):
        print("Fibonacci number at position {position}: {result}".format(position=n, result=fibonacci(n)))

    # Calculate factorial numbers
    for n in range(10):
        print("Factorial of {n}: {result}".format(n=n, result=factorial(n)))

    # Calculate bernoulli numbers
    n = 12
    print("Bernoulli number of {n}: {result}".format(n=n, result=bernoulli(n)))
