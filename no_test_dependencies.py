import pytest
import requests
import twisted
import numpy
import scipy


# Test install of pytest

def square(n):
    return(n*n)
def test_the_function():
    assert square(2) == 4
    assert square(2) == 3

# Test install of requests

r = requests.get('https://github.com/hlpostman/challenges')
print(r.status_code)

# Test install of twisted



# Test install of numpy

a = numpy.floor(10*numpy.random.random((2,2)))
b = numpy.floor(10*numpy.random.random((2,2)))
stacked = numpy.column_stack((a,b))
print(stacked)

# Test install of scipy

scipy_gamma_info = scipy.info("gamma")
print(scipy_gamma_info)
