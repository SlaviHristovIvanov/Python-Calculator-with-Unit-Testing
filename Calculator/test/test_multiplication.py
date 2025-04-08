import pytest

from stuff.calc import Calculator

@pytest.mark.parametrize("a, b, expected", [
    (5, 5, 25),
    (10, 10, 100),
    (2, 8, 16),
    (100, 100, 10000)
])

def test_multiply(calculator, a, b, expected):
    res =calculator.multiply(a, b)
    assert res == expected