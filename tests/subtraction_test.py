""" Subtraction Tests """
import os
import pandas as pd

from calculator.calculations.subtraction import Subtraction

file_path = os.path.dirname(os.path.realpath(__file__))

def subtraction_test_calculation():
    """" testing static method for subtraction """
    # Arrange
    active_file = os.path.join(file_path, "Subtraction Data 1.csv")
    dframe = pd.read_csv(active_file, names=["A", "B", "C"])
    # Act
    for i, row in dframe.iterrows():
        vals = (row.A, row.B)
        subtract = Subtraction.create(vals)
    # Assert
        assert subtract.get_result() == dframe["C"][i]
