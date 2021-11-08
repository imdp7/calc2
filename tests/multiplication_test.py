""" Multiplication Tests """
from calculator.calculations.multiplication import Multiplication


def multiplication_test_calculation():
    """ testing static method for addition """
    # Arrange
    numbers = (10.0, 10.0)
    multiplication = Multiplication(numbers)
    # Act
    # Assert
    assert multiplication.get_result() == 100.0
