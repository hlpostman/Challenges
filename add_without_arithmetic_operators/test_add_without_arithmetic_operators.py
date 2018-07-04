# test_add_without_arithmetic_operators.py
# 28 June 2018

import pytest
from add_without_arithmetic_operators import add_without_arithmetic_operators as add

LARGEST_UNSIGNED_64_BIT_INT = 18446744073709551615

# Test valid input
def test_general_input():
    # No carrying required
    assert add(1,2) == 3 # 0001, 0010 => 0011, effectively a bit-wise "or"
    # Carrying that can be placed in the very next bit
    assert add(2,3) == 5 # 0010, 0011 => 0101
    # Carrying that cannot be placed in the very next bit, but does not require adding 3 bits
    assert add(6,3) == 9 # 0110, 0011 => 1001
    # Carrying that cannot be placed in the very next bit, and requires adding 3 bits
    assert add(7,3) == 10 # 0111, 0011 => 1010

def test_extreme_input():
    # Test symmetric input
    assert add(1,1) == 2
    assert add(500,500) == 1000
    # Test commutativity
    assert add(1,2) == add(2,1)
    assert add(1,2) == 3
    assert add(2,1) == 3
    # Test additive identity (i.e. anything plus 0 should be itself)
    assert add(0,0) == 0
    assert add(0,1) == 1
    # Test large input
    assert add(10000,10000) == 20000
    assert add(1000000000,9000000000) == 10000000000
    # Test overflow
    assert add(LARGEST_UNSIGNED_64_BIT_INT, 1) == 18446744073709551616
    assert add(LARGEST_UNSIGNED_64_BIT_INT, LARGEST_UNSIGNED_64_BIT_INT) == 36893488147419103230



# Test bad input
# Negative numbers, including "-0", floats, non-numeric input, wrong number of arguments
def test_type_error():
    with pytest.raises(TypeError):
        # Bad number of arguments
        add()
        add(1)
        add(1,1,1)
        # Bad type in first argument
        add(1.0, 1)
        add("", 1)
        add([], 1)
        # Bad type in second argument
        add(1, 1.0)
        add(1, "")
        add(1,[])

def test_value_error():
    # Signed input
    with pytest.raises(ValueError):
        add(-1, 1)
    with pytest.raises(ValueError):
        add(1, -1)
