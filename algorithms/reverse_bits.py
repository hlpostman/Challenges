# reverse_bits.py
# 28 May 2018

class ReverseBits:

    def __init__(self):
        self.PRECOMPUTED_HASH_OF_16_BIT_WORDS = self.initialize_hash()

    def initialize_hash(self):
        return({i:self.precompute_reversed_bits(i) for i in range(65535)}) #65,535 is 2^16-1

    def precompute_reversed_bits(self,n):
        """Takes a 16-bit unsigned integer and returns that number with the bits reversed.  Linearly addresses the bits in n, but as n has a constant number of bits, has a constant upper limit of L.

        Args:
            n: a 16-bit unsigned integer

        Returns:
            A 16-bit unsigned integer representing the integer passed but with its bits reversed

        Raises:
            ValueError: n is not a 16-bit integer, but is a numeric type (possibilities include n is larger than 16 bits, a float, or signed)
            TypeError: n is not a numeric type
        """
        reversed = 0
        for i in range(16):
            if (n>>i)&1:
                reversed |= (1<<(15-i))
        return(reversed)

    def reverse_bits(self,n):
        """Takes 64-bit unsigned integer and returns that number with the bits reversed.

        Args:
            n: a 64-bit unsigned integer

        Returns:
            A 64-bit unsigned integer representing the integer passed but with its bits reversed

        Raises:
            ValueError: n is not a 64-bit integer, but is a numeric type (possibilities include n is larger than 64 bits, a float, or signed)
            TypeError: n is not a numeric type
        """
        reversed = 0
        size_16_mask = 0xFFFF
        for i in range(3,-1,-1):
            bit_mask = (n>>16*i)&size_16_mask
            reversed |= (self.PRECOMPUTED_HASH_OF_16_BIT_WORDS[bit_mask])<<16*i
        return(reversed)
