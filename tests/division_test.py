"""Testing Division"""
from calc.calculations.division import Division

def test_calculation_division():
    """testing that our calculator has a static method for division"""
    #Arrange
    mynumbers = (1.0,2.0)
    division = Division(mynumbers)
    #Act
    #Assert
    assert division.get_result() == 0.5
    #Arrange
    mynumbers = (5.0,2.0)
    division = Division(mynumbers)
    #Act
    #Assert
    assert division.get_result() == 2.5
           
