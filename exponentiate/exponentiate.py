# exponentiate.py
# 16 July 2018

def exponentiate(a,b):
    """Takes two numbers a and b, and returns the value of a raised to the power of b, without using **, the Python exponentiation operator.

    Args:
        a: float or integer, the base for the exponentiation.  May be signed or unsigned.
        b: integer, the exponent for the exponentiation.  May be signed or unsigned.

    Returns:
        float, the result of raising a to the power of b

    Raises:
        TypeError:
                1) argument a is neither a float nor an integer (float or integer expected)
                2) argument b is not an integer (integer expected)
                3) wrong number of arguments passed (two expected)
        ValueError: both arguments are zero (at least one nonzero argument expected)
    """
    if a == b == 0:
        raise ValueError("Expected at least one nonzero argument. Given 0 for both arguments.")
    result = 1.0
    if b < 0:
        b, a = -b, 1.0 / a
    while b:
        # Handle the single copy of a held in b if b is odd
        if b & 1:
            result *= a
        a, b = a * a, b >> 1
    return result/1.0
