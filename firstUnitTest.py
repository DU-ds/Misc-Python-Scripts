"""
following tutorials:
https://www.jeffknupp.com/blog/2013/12/09/improve-your-python-understanding-unit-testing/
https://diveinto.org/python3/unit-testing.html
https://docs.pytest.org/en/latest/getting-started.html#install-pytest

see unittest docs for more ideas about tests:
https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug

to run tests:
pytest R:/Git/Misc-Python-Scripts/firstUnitTest.py

"""
# import os
# os.chdir("R:/Git/Misc-Python-Scripts")
# don't think I need them?

import unittest
from primes import is_prime


class PrimesTestCase(unittest.TestCase):
    """Tests for `primes.py`."""

    def test_is_eleven_prime(self):
        """ does it recognize that 11 is prime """
        self.assertTrue(is_prime(11))
    
    def test_zero_is_not_prime(self):
        self.assertFalse(is_prime(0))
    
    def test_negative(self):
        self.assertFalse(is_prime(-1))
    
    def test(self):
        pass


def func(x):
    return x + 2
    
def test_one():
    assert func(3) == 5
    
def test_two():
    x = "hello"
    assert not hasattr(x, "check")


if __name__ == '__main__':
    unittest.main()
    #pytest.main()
    