# test_divide.py
# 15 July 2018

import pytest
from divide import divide

# Test valid input

def test_basic_input():
    # b divides a evenly
    assert divide(10,2) == 5
    assert divide(15,3) == 5
    assert divide(15,5) == 3

    # a does NOT divide b evenly, a > b
    assert divide(10,3) == 3
    assert divide(15,2) == 7

    # a does NOT divide b evenly, a < b
    assert divide(10,11) == 0
    assert divide(15,100) == 0

def test_a_and_b_same_number():
    assert divide(5,5) == 1
    assert divide(1000,1000) == 1

def test_division_by_one():
    assert divide(1,1) == 1
    assert divide(5,1) == 5
    assert divide(1000,1) == 1000

def test_zero_as_dividend():
    assert divide(0,1) == 0
    assert divide(0,2) == 0

def test_large_input():
    assert divide(9223372036854775807,1) # a is max 64-bit unsigned int (2**63 - 1)
    assert divide(10000000000000000000,1000000000000000000) # 10**19 divided by 10**18

# Test bad input

# Test TypeError
def test_float_input():
    # Floored floats
    with pytest.raises(TypeError):
        divide(1.0,1)
    with pytest.raises(TypeError):
        divide(1,1.0)
    # Floats with nonzero decimals
    with pytest.raises(TypeError):
        divide(1.5,1)
    with pytest.raises(TypeError):
        divide(1,1.5)

def test_negative_input():
    with pytest.raises(TypeError):
        divide(-1,1)
    with pytest.raises(TypeError):
        divide(1,-1)

def test_non_numeric_input():
    with pytest.raises(TypeError):
        divide("","")
    with pytest.raises(TypeError):
        divide([],[])
    with pytest.raises(TypeError):
        divide((),{})

def test_wrong_number_of_arguments():
    # No arguments
    with pytest.raises(TypeError):
        divide()
    # Only one argument
    with pytest.raises(TypeError):
        divide(1)
    # More than two arguments
    with pytest.raises(TypeError):
        divide(20,2,5)

# Test ValueError
def test_division_by_zero():
    with pytest.raises(ValueError):
        divide(0,0)
    with pytest.raises(ValueError):
        divide(1,0)
