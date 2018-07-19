# is_palindrome_in_base_ten.py
# 14 July 2018

def is_palindrome(n):
    """ Detects whether or not the digits of n form a palindrome, i.e. whether n reads as the same number in base ten when read from left to right as when read from right to left, e.g. 101.

    Args:
        n: an integer in base ten, signed or unsigned

    Returns:
        bool: True if the digits of n form a palindrome, False if not

    Raises:
        TypeError: n is not an integer
    """
    if not isinstance(n, int):
        raise TypeError("Bad argument type. Expecting integer. Given float.")
    n = -1*n if n < 0 else n
    num_digits = count_digits(n)
    for i in range(num_digits//2):
        front_cmp = (n//10**(num_digits-(i+1)))%10
        back_cmp = (n//10**i)%10
        if front_cmp != back_cmp:
            return False
    return True

def count_digits(n):
    """Counts the number of places, i.e. digits, in the number passed.

    Args:
        n: an integer, signed or unsigned

    Returns:
        integer representing the number of places, i.e. digits, in n, e.g. if n = 123, the return integer is 3.

    Raises:
        TypeError: n is not an integer.  Floats do not work, even they are floored, e.g. 1.0 raises TypeError, 1 does not.
    """

    n = -1*n if n < 0 else n
    num_digits = 0
    while n:
        num_digits += 1
        n //= 10
    return num_digits
