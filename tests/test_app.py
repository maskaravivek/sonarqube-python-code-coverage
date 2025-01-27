import pytest

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from app import add, subtract, multiply, divide


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 10) == -10


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10


def test_divide():
    assert divide(10, 2) == 5
    assert divide(-15, 3) == -5

    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        divide(5, 0)  # Division by zero
