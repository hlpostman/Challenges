# test_divide.py
# 15 July 2018

import pytest
import divide

# Test valid input

# Test extreme input - 0 div anything, large numbers

# Division by 1
# Diviion causing 0 as output
# Division causing floor, divsion not causing floor - two sections with comments in basic input

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

def test_negative_input():
    with pytest.raises(ValueError):
        divide(-1,1)
    with pytest.raises(ValueError):
        divide(1,-1)
