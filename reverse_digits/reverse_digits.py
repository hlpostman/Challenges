# reverse_digits.py
# 11 July 2018

def reverse_digits(n):
    """ Takes an integer and returns an integer that has its digits the reverse from that of the input integer.

    Args:
        n: an integer, signed or unsigned

    Returns:
        integer.  The return integer has its digits the reverse from that of the input integer, e.g if the input integer is 123, returns 321.

    Raises:
        TypeError: n is not an integer
    """
    if not isinstance(n, int):
        raise TypeError("Bad argument type.  Expecting integer.  Given float.")
    n_is_negative = True if n < 0 else False # Handle negative input step 1 of 3
    n = -1*n if n_is_negative else n # Handle negative input step 2 of 3
    reversed_digits = 0

    while n:
        reversed_digits += n%10
        reversed_digits *= 10 # Left shift by 1 place so each digit of n just gets added as a 1's place
        n //= 10

    reversed_digits //= 10 # Shift back right by 1 place

    # Handle negative input step 3 of 3
    reversed_digits = -1*reversed_digits if n_is_negative else reversed_digits #

    return reversed_digits
