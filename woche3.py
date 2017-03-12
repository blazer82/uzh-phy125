"""
    Excercise 3: Prime numbers
"""

import numpy as np
from math import ceil, sqrt, log

def find_upper_bound_to_prime(n):
    """
    Find upper bound to n-th prime number

    Arguments
    ---------
    n: int, n=0 -> 2

    Return
    ------
    int
    """
    if n > 6:
        upper_bound = ceil((n+1) * (log(n+1) + log(log(n+1))))
    else:
        upper_bound = 20
    return upper_bound

def eratosthenes(n):
    """
    Find n prime numbers using Eratosthenes' algorithm

    Arguments
    ---------
    n: int, n=0 -> 2

    Return
    ------
    list, list of n prime numbers
    """

    # Calculate upper bound
    upper_bound = find_upper_bound_to_prime(n)

    # Initialize primes array
    primes = np.zeros(upper_bound + 1) == 0 # Set all entries to True

    # Set non-primes to False according to Eratosthenes' algorithm
    for i in range(2, ceil(sqrt(upper_bound))):
        multiplier = 2
        k = multiplier * i
        while k <= upper_bound:
            primes[k] = False
            multiplier += 1
            k = multiplier * i

    # Find n primes
    position = 0
    known_primes = []
    for i in range(2, len(primes)):
        if primes[i]:
            known_primes.append(i)
            if position == n:
                return known_primes
            position += 1

    raise ValueError("Upper bound too low to find {n} primes!".format(n=n))

def loop_invariant(n):
    """
    Find n prime numbers

    Arguments
    ---------
    n: int, n=0 -> 2

    Return
    ------
    list, list of n prime numbers
    """

    def get_multiples(numbers, infimum):
        result = []
        for entry in numbers:
            multiplier = 1
            number = entry * multiplier
            while number < infimum:
                multiplier += 1
                number = entry * multiplier
            result.append(number)
        return result

    upper_bound = find_upper_bound_to_prime(n)
    known_primes = [2]
    for i in range(3, upper_bound):
        multiples = get_multiples(known_primes, i)
        # Our loop invariant would now be known_primes < i <= multiples
        if not i in multiples:
            known_primes.append(i)
            if len(known_primes) == n + 1:
                return known_primes

    raise ValueError("Upper bound too low to find {n} primes!".format(n=n))


if __name__ == '__main__':
    # Find 115th prime
    print("\nCalculate primes using Eratosthenes...")
    p_115 = eratosthenes(115)[-1]
    print("115th prime number is {number}".format(number=p_115))

    print("\nCalculate primes using loop invariants...")
    p_115 = loop_invariant(115)[-1]
    print("115th prime number is {number}".format(number=p_115))
