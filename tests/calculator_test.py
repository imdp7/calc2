"""Testing the Calculator"""
from calculator.calculator import Calculator

def test_calculator_result():
    """testing calculator result is 0"""
    calc = Calculator()
    assert calc.result == 0

def test_calculator_add():
    assert Calculator.add_number(1,3) == 3

def test_calculator_get_result():
    """Testing the Get result method of the calculator"""
    calc = Calculator()
    assert calc.get_result() == 0

def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    calc = Calculator()
    calc.subtract_number(1)
    assert calc.get_result() == -1
def test_calculator_multiply():
    """ tests multiplication of two numbers"""
    calc = Calculator()
    result  = calc.multiply_numbers(1,2)
    assert result == 2
def test_calculator_divide():
    """ tests multiplication of two numbers"""
    calc = Calculator()
    result  = calc.divide_numbers(4,2)
    assert result == 2
