from fractions import Fraction

def decimal(fraction, n_digits):
    """ turn a fraction object into a decimal fraction string """
    int_part = int(fraction)
    remaining_fraction = fraction - int_part
    digits = int(remaining_fraction*10**n_digits)
    result = ("{int}.{digits:0"+str(n_digits)+"d}").format(int=int_part, digits=digits)
    return result

def arctan(fraction, precision):
    """ calculate arctan using Taylor to a certain precision """
    result = fraction
    numerator = fraction
    denominator = 1
    n = 0
    while True:
        n += 1
        numerator *= fraction**2
        denominator += 2
        result += (-1)**n * Fraction(numerator, denominator)
        if n > precision:
            break
    return result


if __name__ == '__main__':
    p = 768
    feynmanPi = 16 * arctan(Fraction(1, 5), p) - 4 * arctan(Fraction(1, 239), p)
    print(float(feynmanPi))
    print(decimal(feynmanPi, p))
