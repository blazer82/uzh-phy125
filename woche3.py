"""
    Excercise 3: Prime numbers
"""

import numpy as np
from math import ceil, sqrt, log

def eratosthenes(n, sup=None):
    """
    Find n-th prime number using Eratosthenes' algorithm

    Arguments
    ---------
    n: int, n=0 -> 2
    sup: int, upper bound (optional)

    Return
    ------
    int, n-th prime number
    """

    # Calculate upper bound if none provided
    if sup is None:
        if n > 6:
            sup = ceil((n+1) * (log(n+1) + log(log(n+1))))
        else:
            sup = 20
        print("Use upper bound: {number}".format(number=sup))

    # Initialize primes array
    primes = np.zeros(sup + 1) == 0 # Set all primes to True

    # Set non-primes to False according to Eratosthenes' algorithm
    for i in range(2, ceil(sqrt(sup))):
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
    p_115 = eratosthenes(115)
    print("115th prime number is {number}".format(number=p_115))
