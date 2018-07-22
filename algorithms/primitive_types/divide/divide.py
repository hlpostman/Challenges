# divide.py
# 18 July 2018

def divide(a,b):
    """Returns the quotient of a divided by b using -,+, <<, and >> rather than /, //, or %, without remainder.

    Args:
        a: unsigned integer
        b: positive integer

    Returns:
        unsigned integer, the integer portion of a divided by b, i.e. the floor of a divided by b, e.g. if a is 5 and b is 2, returns 2.

    Raises:
        TypeError: expecting unsigned integers
        ValueError: b is zero, division by which is undefined
    """
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Bad type. Expected unsigned integer.")
    if a < 0 or b < 0:
        raise TypeError("Expected unsigned integers. Given signed value.")
    if b == 0:
        raise ValueError("Expected positive integer for second argument. Given 0.")
    quotient, max_power_of_2_in_b = 0, 64
    max_multiple_of_b_in_a = b << max_power_of_2_in_b
    while a >= b:
        while max_multiple_of_b_in_a > a:
            max_multiple_of_b_in_a >>= 1
            max_power_of_2_in_b -= 1
        quotient += 1 << max_power_of_2_in_b
        a -= max_multiple_of_b_in_a
    return quotient
