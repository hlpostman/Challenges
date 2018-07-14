# is_palindrome_in_base_ten.py
# 14 July 2018

def is_palindrome(n):
    """ Detects whether or not the digits of n form a palindrome, i.e. whether n reads as the same number in base ten when read from left to right as when read from right to left, e.g. 101.

    Args:
        n: an integer in base ten

    Returns:
        bool: True if the digits of n form a palindrome, False if not

    Raises:
        TypeError: n is not an integer
    """
    if not isinstance(n, int):
        raise TypeError("Bad argument type. Expecting integer. Given float.")
    n = -1*n if n < 0 else n
    num_digits = 0
    i = 1
    while n//i != 0:
        num_digits += 1
        i *= 10
    del i
    for i in range(num_digits//2):
        front_cmp = (n//10**(num_digits-(i+1)))%10
        back_cmp = (n//10**i)%10
        print(i, front_cmp, back_cmp)
        if front_cmp != back_cmp:
            return False
    return True
