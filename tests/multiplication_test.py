""" Multiplication Tests """
import os
import pandas as pd

from calculator.calculations.multiplication import Multiplication

file_path = os.path.dirname(os.path.realpath(__file__))

def multiplication_test_calculation():
    """ testing static method for addition """
    # Arrange
    active_file = os.path.join(file_path, "Multiplication Data 1.csv")
    dframe = pd.read_csv(active_file, names=["A", "B", "C"])
    # Act
    for i, row in dframe.iterrows():
        vals = (row.A, row.B)
        multiply = Multiplication.create(vals)
    # Assert
        assert multiply.get_result() == dframe["C"][i]
