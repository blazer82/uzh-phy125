"""
    Excercise 3: Prime numbers
"""

import numpy as np
from math import ceil

def eratosthenes(n, sup):
    """
    Find n-th prime number using Eratosthenes' algorithm

    Arguments
    ---------
    n: int, n=0 -> 2
    sup: int, upper bound

    Return
    ------
    int, n-th prime number
    """

    primes = np.zeros(sup + 1) == 0 # Set all primes to True

    # Set non-primes to False according to Eratosthenes' algorithm
    for i in range(2, ceil(sup / 2)):
        multiplier = 2
        k = multiplier * i
        while k <= sup:
            primes[k] = False
            multiplier += 1
            k = multiplier * i

    # Find n-th prime
    position = 0
    for i in range(2, len(primes)):
        if primes[i]:
            if position == n:
                return i
            position += 1

    raise ValueError("Upper bound too low to find {n}-th prime!".format(n=n))

if __name__ == '__main__':
    # Find 115th prime
    p_115 = eratosthenes(115, 1000)
    print("115th prime number is {number}".format(number=p_115))
