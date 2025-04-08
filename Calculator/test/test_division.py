import pytest

from stuff.calc import Calculator

@pytest.mark.parametrize("a, b, expected", [
    (100, 10, 10),
    (25, 5, 5),
    (81, 9, 9)
])

def test_division(calculator, a, b, expected):
    res = calculator.divide(a, b)
    assert res == expected

@pytest.mark.parametrize("a, b", [
    (100, 0),
    (0, 5),
    (-1, 0)
])

def test_division_by_zero(calculator, a, b):
    if b == 0:
        with pytest.raises(ZeroDivisionError):
            calculator.divide(a, b)
    else:
        res = calculator.divide(a, b)
        assert res == a / b

@pytest.mark.parametrize("a, b", [
    (40, -20),
    (20, -2),
    (-10, 7)
])
def test_divide_negative_numbers(calculator, a, b):
    res = calculator.divide(a, b)
    assert res == a / b