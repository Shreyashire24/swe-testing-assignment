import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculator import add, subtract, multiply, divide, clear

def test_add_positive():
    assert add(5, 3) == 8

def test_subtract_positive():
    assert subtract(10, 4) == 6

def test_multiply_positive():
    assert multiply(6, 7) == 42

def test_divide_positive():
    assert divide(10, 2) == 5.0

def test_divide_by_zero():
    try:
        divide(5, 0)
        assert False
    except ValueError:
        assert True

def test_add_negative_numbers():
    assert add(-3, -7) == -10

def test_multiply_decimal():
    assert multiply(2.5, 4) == 10.0

def test_large_numbers():
    assert add(1000000, 2000000) == 3000000

def test_clear():
    assert clear() == 0

def test_full_calculation_sequence():
    result = add(5, 3)
    assert result == 8

def test_clear_after_calculation():
    result = multiply(6, 7)
    assert result == 42
    reset = clear()
    assert reset == 0