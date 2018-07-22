# test_is_palindrome_in_base_ten.py
# 14 July 2018

import pytest
from is_palindrome_in_base_ten import is_palindrome

# Test valid input
def test_basic_input():
    assert is_palindrome(10) == False
    assert is_palindrome(11) == True
    assert is_palindrome(111) == True
    assert is_palindrome(11011) == True
    # Negative input
    assert is_palindrome(-11011) == True

def test_extreme_input():
    assert is_palindrome(1) == True # Singleton palindrome
    assert is_palindrome(-9223372036854775807) == False # Min 64-bit integer (2**63 - 1)
    assert is_palindrome(18446744073709551615) == False # Max unsigned 64-bit int (2**64 - 1)
    assert is_palindrome(123456789010987654321) == True # Greater than max int

# Test bad input

# Test TypeError for non-integer input
def test_float_input():
    with pytest.raises(TypeError):
        is_palindrome(1.5)

def test_non_numeric_input_1():
    with pytest.raises(TypeError):
        is_palindrome("")

def test_non_numeric_input_2():
    with pytest.raises(TypeError):
        is_palindrome([])

# Test TypeError with wrong number of arguments
def test_wrong_number_of_arguments_1():
    # No argument passed
    with pytest.raises(TypeError):
        is_palindrome()

def test_wrong_number_of_arguments_2():
    # Too many arguments passed
    with pytest.raises(TypeError):
        is_palindrome(11,11)
