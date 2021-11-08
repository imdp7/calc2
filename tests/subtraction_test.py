""" Subtraction Tests """
from calculator.calculations.subtraction import Subtraction


def subtraction_test_calculation():
    """" testing static method for subtraction """
    # Arrange
    numbers = (10.0, 10.0)
    subtraction = Subtraction(numbers)
    # Act
    # Assert
    assert subtraction.get_result() == 0
