"""
    Exercise 4a: Newton-Raphson
"""

def f(x):
    """
        Our target function f(x)
    """
    return x**3 + x - 40

def f_prime(x):
    """
        First derivative of f(x) --> f'(x)
    """
    return 3 * x**2 + 1


if __name__ == '__main__':

    # Find x for f(x)=0 using Newton-Raphson algorithm

    x = 3 # Initial approximation of x**3+x=30

    iterations = []
    while not x in iterations:
        iterations.append(x)
        x = x - f(x)/f_prime(x)

    print("\nf(x)=0 for x={x}\n".format(x=x))
