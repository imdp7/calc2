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

def test_calculator_add():
    """Testing the Add function of the calculator"""
    # Arrange
    value_a = 1
    value_b = 2
    # Act
    result = Calculator.add_number(value_a,value_b)
    # Assert
    assert result == 3

def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    # Arrange
    value_a = 1
    value_b = 2
    # Act
    result = Calculator.subtract_number(value_a, value_b)
    # Assert
    assert result == -1

def test_calculator_multiply():
    """ Testing multiplication of two numbers"""
    # Arrange
    value_a = 1
    value_b = 2
    # Act
    result = Calculator.multiply_numbers(value_a, value_b)
    # Assert
    assert result == 2

def test_calculator_division():
    """ Testing division of two numbers"""
    # Arrange
    value_a = 1
    value_b = 1
    # Act
    result = Calculator.divide_numbers(value_a, value_b)
    # Assert
    assert result == 1

def test_calculator_division_exception():
    """ Testing division exception for division by zero"""
    # Arrange
    value_a = 1
    value_b = 0
    # Act
    with pytest.raises(ZeroDivisionError):
        Calculator.divide_numbers(value_a,value_b)
