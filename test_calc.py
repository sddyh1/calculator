import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


def test_addition(calc):
    assert calc.evaluate("2 + 3") == 5


def test_subtraction(calc):
    assert calc.evaluate("10 - 4") == 6


def test_multiplication(calc):
    assert calc.evaluate("3 * 4") == 12


def test_division(calc):
    assert calc.evaluate("10 / 2") == 5


def test_precedence(calc):
    assert calc.evaluate("2 + 3 * 4") == 14


def test_parentheses(calc):
    assert calc.evaluate("(2 + 3) * 4") == 20


def test_invalid_char_raises(calc):
    with pytest.raises(ValueError):
        calc.evaluate("2 + import os")