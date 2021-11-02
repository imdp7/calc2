"""Testing the Calculator"""
import pytest
from calculator.calculator import Calculator

def test_calculator_result():
    """testing calculator result is 0"""
    calc = Calculator()
    assert calc.result == 0

def test_calculator_add():
    """ tests the addition between 2 numbers """
    assert Calculator.add_number(5, 5)

def test_calculator_get_result():
    """Testing the Get result method of the calculator"""
    calc = Calculator()
    assert calc.get_result() == 0

def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    assert Calculator.subtract_number(10, 5) == 5

def test_calculator_multiply():
    """ tests multiplication of two numbers"""
    assert Calculator.multiply_numbers(5, 2) == 10

def test_calculator_divide():
    """ tests multiplication of two numbers"""
    assert Calculator.divide_numbers(10, 2) == 5

def test_calculator_division_error():
    """ tests dividing by 0 exception """
    with pytest.raises(ZeroDivisionError):
        Calculator.divide_numbers(1,0)
