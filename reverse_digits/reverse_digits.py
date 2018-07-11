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

    reversed_digits = 0
    num_digits = count_digits(n)

    for i in range(1, num_digits+1):
        reversed_digits += n%10
        reversed_digits *= 10 # Left shift n by 1 place so each digit of n just gets added as a 1's place
        n //= 10

    return reverse_digits

def count_digits(n):
    """Counts the number of places, i.e. digits, in the number passed.

    Args:
        n: an integer, signed or unsigned

    Returns:
        integer representing the number of places, i.e. digits, in n, e.g. if n = 123, the return integer is 3.

    Raises:
        TypeError: n is not an integer.  Floats do not work, even they are floored, e.g. 1.0 raises TypeError, 1 does not.
    """

    num_digits = 0
    while n:
        num_digits += 1
        n //= 10

    return num_digits
