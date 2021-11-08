"""Testing the Calculator"""
import pytest
from calculator.calculator import Calculator
from calculator.history.calculations import Calculation


@pytest.fixture
def clear_history_fixture():
    """ clears history after each run """
    # pylint: disable=redefined-outer-name
    Calculation.empty_history()


def test_calculator_add_static(clear_history_fixture):
    """ tests the addition between 2 numbers """
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.add_number(4.0, 2.0, 1.0) == 7.0


def test_calculator_subtract_static(clear_history_fixture):
    """Testing the subtract method of the calculator"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.subtract_number(10.0, 5.0, 1.0) == -16


def test_calculator_multiply_static(clear_history_fixture):
    """ tests multiplication of two numbers"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.multiply_numbers(5.0, 2.0) == 10.0


def test_calculator_divide_static(clear_history_fixture):
    """ tests multiplication of two numbers"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.divide_numbers(2.0, 10.0) == 5.0
