# test_multiply_without_arithmetic_operators.py
# 14 July 2018

import pytest
from multiply_without_arithmetic_operators import multiply_without_arithmetic_operators as multiply

# Test valid input

def test_basic_input():
    assert multiply(2,3) == 6
    assert multiply(3,3) == 9 # Edge case where a = b
    assert multiply(10, 50) == 500
    
def test_multiplicative_identity():
    assert multiply(1,1) == 1
    assert multiply(1,2) == 2
    assert multiply(1, 5000) == 5000

def test_multiplication_by_zero():
    assert multiply(0,1) == 0
    assert multiply(0,123) == 0

def test_large_input():
    assert multiply(3,6148914691236517205) == 18446744073709551615 # Max unsigned 64-bit int (2**63 - 1)
    assert multiply(2, 18446744073709551615) == 36893488147419103230 # Twice the max unsgned 64-bit int. No overflow due to Python 3's arbitrary precision handling of integers.

def test_commutativity():
    assert multiply(1,2) == multiply(2,1)
    assert multiply(2,3) == multiply(3,2)


# Test bad input

# Test TypeError
def test_float_input():
    with pytest.raises(TypeError):
        multiply(1.0,1)
    with pytest.raises(TypeError):
        multiply(1.56,1)

def test_non_numeric_input():
    with pytest.raises(TypeError):
        multiply("", "")
    with pytest.raises(TypeError):
        multiply([], [])
    with pytest.raises(TypeError):
        multiply((),{})

def test_wrong_number_of_arguments_():
    # No arguments
    with pytest.raises(TypeError):
        multiply()
    # Only one argument
    with pytest.raises(TypeError):
        multiply(1)
    # Too many arguments
    with pytest.raises(TypeError):
        multiply(1,2,3)

# Test ValueError
def test_negative_input():
    with pytest.raises(ValueError):
        multiply(-1,2)
    with pytest.raises(ValueError):
        multiply(2,-1)
