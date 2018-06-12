import pytest
from algorithms.reverse_bits import ReverseBits

class TestReverseBits:



    # Test valid input

    def test_basic_input_precompute(self):
        assert RB.precompute_reversed_bits(1) == 32768


    def test_symmetry(self):

        assert RB.precompute_reversed_bits(1) == 32768
        assert RB.precompute_reversed_bits(32768) == 1



    # def test_symmetry(self):
    # # If reversing the bits in a given number n gives m, reversing the bits in m
    # # should give n
    #
    #     assert RB.reverse_bits(4) == 2305843009213693952
    #     assert RB.reverse_bits(2305843009213693952) == 4

    # def test_extreme_input(self):
    #
    #     assert RB.reverse_bits(0) == 0
    #     # Max integer for unsigned 64-bit, the sum of 2**i where i goes from 0 to 63
    #     assert RB.reverse_bits(18446744073709551615) == 18446744073709551615
    #     # Only bit set is one of two splitting center i.e. 31st or 32nd
    #     assert RB.reverse_bits(4294967296) == 2147483648
    #
    # # Test bad input
    #
    # def test_bad_input(self):
    #     with pytest.raises(ValueError):
    #
    #         RB.reverse_bits(1.0)
    #         RB.reverse_bits(-1)
    #
    # def test_bad_input1(self):
    #     with pytest.raises(TypeError):
    #
    #         RB.reverse_bits([])
    #         RB.reverse_bits("")
