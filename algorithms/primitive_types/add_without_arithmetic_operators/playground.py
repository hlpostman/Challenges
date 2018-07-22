def add_without_arithmetic_operators(a, b):
    """ Takes two unsigned integers and returns their sum without using arithmetic operators.
        Args:
            a, b: both unsigned integers

        Returns:
            an unsigned integer the sum of a and b

        Raises:
            TypeError: at least one of a and b is not an unsigned integer
    """
    if a < 0 or b < 0:
        raise ValueError("Both arguments must be non-negative.")
    print("At outset, your binary strings are \na = %s, b = %s"%(bin(a),bin(b)))
    while b != 0:
        carry = a & b # Mask of the bits that will necessitate carrying
        print("carry = a&b ==> %s"%bin(carry))
        a ^= b # Mask of the bits that, at this iteration, can be added into a from b without carrying
        print("a ^= b ==> %s"%bin(a))
        b = carry << 1 # Carry all of the carry bits one place to the left
        print("b = carry << 1 ==> %s"%bin(b))
    print("Final answer a = %s"%bin(a))
    return a

def main():
  a = eval(input("Give me the first number: "))
  b = eval(input("Give me the second number: "))
  add_without_arithmetic_operators(a,b)
  print(a, "\n", add_without_arithmetic_operators(a,b), "\n", a)

main()
