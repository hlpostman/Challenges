import pytest
from algorithms.reverse_bits import reverse_bits

# Test valid input

def test_symmetry():
# If reversing the bits in a given number n gives m, reversing the bits in m
# should give n
    assert reverse_bits(4) == 2305843009213693952
    assert reverse_bits(2305843009213693952) == 4

def test_extreme_input():
    assert reverse_bits(0) == 0
    # Max integer for unsigned 64-bit, the sum of 2**i where i goes from 0 to 63
    assert reverse_bits(18446744073709551615) == 18446744073709551615
    # Only bit set is one of two splitting center i.e. 31st or 32nd
    assert reverse_bits(4294967296) == 2147483648

# Test bad input

def test_bad_input():
    with pytest.raises(ValueError):
        reverse_bits(1.0)
        reverse_bits(-1)

def test_bad_input1():
    with pytest.raises(TypeError):
        reverse_bits([])
        reverse_bits("")
