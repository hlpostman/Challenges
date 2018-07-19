



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
---
LSB_LOOKUP_TABLE = {2**i:i for i in range(64)}
carry = 0
product = 0
while b:
    # Left shift a by x places, where x is the place of the LSB in b
    LSB_in_b = LSB_LOOKUP_TABLE[b&~(b-1)] # Clear that LSB
    # carry = a & (a<<LSB_in_b)
    a_times_LSB_in_b = a << LSB_in_b
    product += a_times_LSB_in_b
    b &= b-1 # Clear the LSB
return product
