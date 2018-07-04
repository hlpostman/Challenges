# add_without_arithmetic_operators.py
# 3 July 2018

def add_without_arithmetic_operators(a, b):
    """ Takes two unsigned integers and returns their sum without using arithmetic operators.
        Args:
            a, b: both unsigned integers

        Returns:
            an unsigned integer the sum of a and b

        Raises:
            TypeError: at least one of a and b is not an unsigned integer
    """

    while b != 0:
        carry = a & b # Mask of the bits that will necessitate carrying
        a ^= b # Mask of the bits that, at this iteration, can be added into a from b without carrying
        b = carry << 1 # Carry all of the carry bits one place to the left
    return a
