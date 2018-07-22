# test_longest_consecutive_sequence.py
# 22 July 2018

import pytest
from longest_consecutive_sequence import longest_consecutive_sequence as lcs

# Test valid input

def test_basic_input():
    assert lcs([-2,0,100,1,8,-1,9]) == [-2,-1,0,1]

# Test bad input
