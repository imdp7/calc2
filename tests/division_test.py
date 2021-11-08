""" Division Tests """
from calculator.calculations.division import Division


def division_test_calculation():
    """ Testing static method for division """
    # Arrange
    numbers = (15.0, 3.0)
    division = Division(numbers)
    # Act
    # Assert
    assert division.get_result() == 5.0
