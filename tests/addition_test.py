""" Addition Tests """
import os
import pandas as pd

from calculator.calculations.addition import Addition

file_path = os.path.dirname(os.path.realpath(__file__))

def addition_test_calculation():
    """ testing static method for addition """
    # Arrange
    active_file = os.path.join(file_path, "Addition Data 1.csv")
    dframe = pd.read_csv(active_file, names=["A", "B", "C"])
    # Act
    for i, row in dframe.iterrows():
        vals = (row.A, row.B)
        add = Addition.create(vals)
    # Assert
        assert add.get_result() == dframe["C"][i]
