import pytest

from  stuff.calc import Calculator

@pytest.mark.parametrize("a, b, expected", [
    (5, 5000, 5005),
    (100, 100, 200),
    (1000000000, 21211313, 1021211313)
])

def test_addition(calculator, a, b, expected):
    res = calculator.addition(a, b)
    assert res == expected
