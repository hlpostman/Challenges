# multiply_without_arithmetic_operators.py
# 14 July 2018

def multiply_without_arithmetic_operators(a, b):
    """Takes two unsigned integers and returns their product without using arithmetic operators.

    Args:
        a, b: both unsigned integers

    Returns:
        an unsigned integer the product of a and b

    Raises:
        TypeError: the arguments received for a and b are not both integers

    """
    product = 0
    LSB_in_b_mask = 1
    i = 0
    while b:
        if b&LSB_in_b_mask:
            a_times_LSB_in_b = a << i
            product = add_without_arithmetic_operators(product, a_times_LSB_in_b)
            b ^= LSB_in_b_mask # Clear that place in b
        LSB_in_b_mask <<= 1
        i = add_without_arithmetic_operators(i, 1)
    return product

def add_without_arithmetic_operators(a, b):
    """ Takes two unsigned integers and returns their sum without using arithmetic operators.
        Args:
            a, b: both unsigned integers
        Returns:
            an unsigned integer the sum of a and b
        Raises:
            TypeError: the arguments received for a and b are not both integers
    """
    if a < 0 or b < 0:
        raise ValueError("Both arguments must be non-negative.")
    while b != 0:
        carry = a & b # Mask of the bits that will necessitate carrying
        a ^= b # Mask of the bits that, at this iteration, can be added into a from b without carrying
        b = carry << 1 # Carry all of the carry bits one place to the left
    return a
