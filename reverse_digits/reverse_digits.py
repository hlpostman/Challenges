# reverse_digits.py
# 11 July 2018

def reverse_digits(n):
    """ Takes an integer and returns an integer that has its digits the reverse from that of the input integer.

    Args:
        n: an integer, signed or unsigned

    Returns:
        integer.  The return integer has its digits the reverse from that of the input integer, e.g if the input integer is 123, the return integer is 321.  Note tricky values such as 100.  The reverse of digits 1,0, and 0 is 0, 0, and 1 = but 001 is simply 1, therefore the return integer may not have the same number of digits as the input integer.
    Raises:
        TypeError: n is not an integer.  Floats do not work, even they are floored, e.g. 1.0 raises TypeError, 1 does not.
    """

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
