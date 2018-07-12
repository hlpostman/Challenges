handle negative input because while 1 // 10 is 0, -1 // 10 is -1 and would create an infinite loop
we like the expression, for i in range(num_digits-1, -1, -1):
    reversed_digits += (10**i) * (n%10), of what's really going on, but it takes 3x as long about .95 seconds vs 3.25 seconds

"""python

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
    num_digits = count_digits(n)
    reversed_digits = 0

    for i in range(num_digits-1, -1, -1):
        reversed_digits += (10**i) * (n%10)
        n //= 10

    # Handle negative input step 3 of 3
    reversed_digits = -1*reversed_digits if n_is_negative else reversed_digits #

    return reversed_digits


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

nh = timeit.timeit(stmt = no_helper, number = 1000000)
h = timeit.timeit(stmt = helper, number = 1000000)
print(nh, h)
"""

big o and space (linear and constant, respectively, address linear vs constant)

[reverse_digits](https://github.com/hlpostman/challenges/blob/master/reverse_digits/reverse_digits.py)
