import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'assignment folder')))
from even_check import is_even

def test_even_cases():
    assert is_even(2) == True
    assert is_even(4) == True
    assert is_even(0) == True

def test_odd_cases():
    assert is_even(1) == False
    assert is_even(3) == False
