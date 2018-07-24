# test_rectangle_intersection.py
# 24 July 2018

import pytest
from rectangle_intersection import rectangle_intersection as intersection

# Test valid input

def test_boundary_intersection():
    assert intersection((0,0),(1,1),(1,1),(3,3)) == [(1,1),(1,1)]
    assert intersection((0,0),(1,1),(1,0),(1,3)) == [(1,0),(1,1)]

def test_partial_intersection():
    assert intersection((0,0),(10,10),(1,1),(30,30)) == [(1,1),(10,10)]
    assert intersection((0,0),(10,10),(1,1),(8,30)) == [(1,1),(8,10)]

def test_completely_contained():
    assert intersection((0,0),(1,1),(0,0),(1,1)) == [(0,0),(1,1)]
    assert intersection((0,0),(10,10),(2,2),(3,3)) == [(2,2),(3,3)]

def test_no_intersection():
    assert intersection((0,0),(1,1),(2,2),(3,3)) == [(float('inf'),float('inf')),(float('inf'),float('inf'))]

def test_argument_symmetry():
    # Whether the first two arguments are for rectangle A or B doesn't matter
    assert intersection((0,0),(10,10),(1,1),(30,30)) == intersection((1,1),(30,30),(0,0),(10,10))
    assert intersection((0,0),(10,10),(2,2),(3,3)) == intersection((2,2),(3,3),(0,0),(10,10))
    assert intersection((0,0),(1,1),(2,2),(3,3)) == intersection((2,2),(3,3),(0,0),(1,1))

# Test bad input
