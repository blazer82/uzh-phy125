"""
    Excercise 2: Bernoulli

    Optimized versions of included functions
"""

from fractions import Fraction

# Use caches to trade cpu time for memory
fibonacci_cache = [1, 1]
bernoulli_cache = [Fraction(1, 1)]

def fibonacci(n):
    """
    Calculate n-th Fibonacci number (cpu time optimized)

    Arguments
    ---------
    n: int

    Return
    ------
    int, n-th Fibonacci number
    """
    # Use cache if possible
    if n < len(fibonacci_cache):
        return fibonacci_cache[n]

    # Calculate and build cache
    fibonacci_cache.append(fibonacci(n-1) + fibonacci(n-2))
    return fibonacci_cache[n]

def factorial(x):
    """
    Calculate factorial (tail recursion optimized)

    Arguments
    ---------
    x: int

    Return
    ------
    int, calculated factorial of x
    """
    result = 1
    for i in range(1, x+1):
        result *= i
    return result

def bernoulli(n):
    """
    Calculate n-th Bernoulli number (cpu time optimized)

    Arguments
    ---------
    n: int

    Return
    ------
    Fraction, n-th Bernoulli number
    """
    # Use cache if possible
    if n <= len(bernoulli_cache) - 1:
        return bernoulli_cache[n]

    # Calculate and build cache
    b_sum = Fraction(0, 1)
    n_factorial = factorial(n)
    for k in range(n):
        b_sum += Fraction(n_factorial * bernoulli(k), factorial(k) * factorial(n-k+1))

    bernoulli_cache.append(-b_sum)
    return bernoulli_cache[n]


if __name__ == '__main__':
    # Calculate fibonacci numbers
    for n in range(10):
        print("Fibonacci number at position {position}: {result}".format(position=n, result=fibonacci(n)))

    # Calculate factorial numbers
    for n in range(10):
        print("Factorial of {n}: {result}".format(n=n, result=factorial(n)))

    # Calculate bernoulli numbers
    n = 20
    print("Bernoulli number of {n}: {result}".format(n=n, result=bernoulli(n)))
