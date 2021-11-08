""" Addition Tests """
from calculator.calculations.addition import Addition


def addition_test_calculation():
    """ testing static method for addition """
    # Arrange
    numbers = (5.0, 10.0)
    addition = Addition(numbers)
    # Act
    # Assert
    assert addition.get_result() == 15.0
