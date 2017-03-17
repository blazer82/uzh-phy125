"""
    Excercise 1: Machin's formula

    Calculate Pi to a precision of at least 762 (Feynman point)
"""

from fractions import Fraction

def decimal(fraction, n_digits):
    """
    Turn a fraction object into a decimal fraction string

    Arguments
    ---------
    fraction: Fraction object
    n_digits: int, number of digits to return

    Return
    ------
    string, decimal fraction
    """
    int_part = int(fraction)
    remaining_fraction = fraction - int_part
    digits = int(remaining_fraction*10**n_digits)
    result = ("{int}.{digits:0"+str(n_digits)+"d}").format(int=int_part, digits=digits)
    return result

def arctan(fraction, precision):
    """
    Calculate arctan using Taylor to a certain precision

    Arguments
    ---------
    fraction: Fraction object
    precision: int

    Return
    ------
    Fraction object
    """
    result = fraction
    numerator = fraction
    denominator = 1
    for n in range(precision):
        numerator *= fraction**2
        denominator += 2
        result += (-1)**(n+1) * Fraction(numerator, denominator)
    return result


if __name__ == '__main__':
    p = 768
    feynmanPi = 16 * arctan(Fraction(1, 5), p) - 4 * arctan(Fraction(1, 239), p)
    print("Pi to a precision of {p}:".format(p=p))
    print(decimal(feynmanPi, p))
