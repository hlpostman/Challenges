# test_reverse_digits.py
# 11 July 2018

import pytest
from reverse_digits import reverse_digits as reverse


# Test valid input

def test_basic_input():
    assert reverse(123) == 321
    assert reverse(12345678901) == 10987654321

def test_extreme_size_input():
    assert reverse(1) == 1 # Singleton palindrome
    assert reverse(-9223372036854775807) == -7085774586302733229 # Min 64 bit int -(2**63 - 1)
    assert reverse(18446744073709551615) == 51615590737044764481 # Max unsigned 64-bit int (2**64-1)

def test_input_ending_in_zero():
    assert reverse(10) == 1
    assert reverse(10000) == 1
    assert reverse(1010) == 101

def test_palindromic_input():
    # The singleton palindrome tested in test_extreme_size_input()
    assert reverse(11) == 11
    assert reverse(1001) == 1001

# Test bad input

# Test TypeError for non-integer input
def test_float_input():
    with pytest.raises(TypeError):
        reverse(123.0)

def test_non_numeric_input_1():
    with pytest.raises(TypeError):
        reverse("")

def test_non_numeric_input_2():
    with pytest.raises(TypeError):
        reverse([])

# Test TypeError for wrong number of arguments
def test_wrong_number_of_arguments_1():
    # No argument passed
    with pytest.raises(TypeError):
        reverse()

def test_wrong_number_of_arguments_2():
    # Too many arguments passed
    with pytest.raises(TypeError):
        reverse(123,123)
