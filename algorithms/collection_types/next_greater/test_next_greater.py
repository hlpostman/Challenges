# test_next_greater.py
# 22 July 2018

import pytest
from next_greater import next_greater as ng

# Test valid input
def test_basic_input():
    assert ng([1,2,3]) == [2,3,-1]
    assert ng([-3,-2,-1]) == [-2,-1,-1]
    assert ng([1,9,4,3,10]) == [9,10,10,10,-1]
    assert ng([4,5,2,10]) == [5,10,10,-1]
def test_extreme_input():
    # Singleton list
    assert ng([1]) == [-1]
    # Multiple elements, no next greater for any element
    assert ng([1,1,1]) == [-1,-1,-1]
    # Large input
    large_input = [i for i in range(100000,0,-1)]
    assert ng(large_input) == [-1 for _ in range(100000)]


# Test bad input
