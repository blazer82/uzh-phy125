"""
    Excercise 3: Prime numbers

    Additional exercise: Primzahlensatz
"""

import numpy as np
import matplotlib.pyplot as plt
from woche3 import eratosthenes, loop_invariant


if __name__ == '__main__':
    number_of_primes = 10000

    print("\nCalculate primes using Eratosthenes...")
    primes = np.array(eratosthenes(number_of_primes, return_list=True))

    # print("\nCalculate primes using loop invariants...")
    # primes = np.array(loop_invariant(number_of_primes, return_list=True))

    print("Highest prime found: {prime}".format(prime=primes[-1]))

    # Calculate log of primes
    log_p = np.log(primes)

    # Calculate ratio between primes and their log
    ratio = primes / log_p

    # Normalize ratio by k
    prime_range_k = np.array(range(1, number_of_primes + 2))
    ratio_normalized = ratio / prime_range_k

    # Plot ratio
    plt.title("Primzahlensatz")
    plt.xlabel("k")
    plt.ylabel("P_k/(k*log(P_k))")
    plt.plot(prime_range_k, ratio_normalized, '-')
    plt.ylim([.75, 1.25])
    plt.savefig('primzahlensatz.pdf')
    plt.show()
