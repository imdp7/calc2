""" Division Tests """
import os
import pandas as pd

from calculator.calculations.division import Division

file_path = os.path.dirname(os.path.realpath(__file__))


def division_test_calculation():
    """ Testing static method for division """
    # Arrange
    active_file = os.path.join(file_path, "Division Data 1.csv")
    dframe = pd.read_csv(active_file, names=["A", "B", "C"])
    # Act
    for i, row in dframe.iterrows():
        vals = (row.A, row.B)
        divide = Division.create(vals)
    # Assert
        assert divide.get_result() == dframe["C"][i]
