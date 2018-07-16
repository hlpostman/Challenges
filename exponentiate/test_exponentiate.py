# test_exponentiate.py
# 15 July 2018

import pytest
from exponentiate import exponentiate

# Test valid input

def test_basic_input():
    assert exponentiate(2,2) == 4 # Edge case where base and exp are same
    assert exponentiate(2,3) == 8
    assert exponentiate(5,10) == 9765625

def test_power_of_zero():
    assert exponentiate(2,0) == 1
    assert exponentiate(1000,0) == 1

def test_power_of_one():
    assert exponentiate(2,1) == 2
    assert exponentiate(1000,1) == 1000

def test_bases_with_invariant_output():
    # Base of 0
    assert exponentiate(0,1) == 0
    assert exponentiate(0,1000) == 0
    # Base of 1
    assert exponentiate(1,1) == 1
    assert exponentiate(1,0) == 1
    assert exponentiate(1,1000) == 1

def test_large_input():
    assert exponentiate(10000,10) == 10000.0**10
    assert exponentiate(4294967296,2) == 18446744073709551616 # Result excedes max unsigned 64-bit int of 18446744073709551615 (2**63 - 1)

def test_float_base_input():
    assert exponentiate(0.5,2) == 0.25
    assert exponentiate(2.5,2) == 6.25

def test_negative_base_input():
    assert exponentiate(-2,2) == 4
    assert exponentiate(-2,3) == -8

def test_negative_exponent_input():
    assert exponentiate(2,-2) == 0.25
    assert exponentiate(-2,-2) == 0.25
    assert exponentiate(-2,-3) == -0.125

# Test bad input

# Test TypeError
def test_float_exponent_input():
    # Floored floats
    with pytest.raises(TypeError):
        exponentiate(1,1.0)
    # # Floats with nonzero decimals
    with pytest.raises(TypeError):
        exponentiate(1,1.5)

def test_non_numeric_input():
    with pytest.raises(TypeError):
        exponentiate("","")
    with pytest.raises(TypeError):
        exponentiate([],[])
    with pytest.raises(TypeError):
        exponentiate((),{})

def test_wrong_number_of_arguments():
    # No arguments
    with pytest.raises(TypeError):
        exponentiate()
    # Only one argument
    with pytest.raises(TypeError):
        exponentiate(1)
    # More than two arguments
    with pytest.raises(TypeError):
        exponentiate(1,2,3)

# Test ValueError
def test_zero_passed_for_both_arguments():
    # Zero to the zero is undefined
    with pytest.raises(ValueError):
        exponentiate(0,0)
    with pytest.raises(ValueError):
        exponentiate(0.0,0.0)
