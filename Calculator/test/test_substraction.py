import pytest

from  stuff.calc import Calculator

@pytest.mark.parametrize("a, b, expected", [
    (1000, 1, 999),
    (10, 12, -2),
    (2000, 20.0, 1980.0),
    (387, 0.9, 386.1)
])

def test_substraction(calculator, a, b, expected):
    res = calculator.substract(a, b)
    assert res == expected