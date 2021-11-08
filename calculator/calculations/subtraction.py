""" subtracts two numbers """
import pprint
from calculator.calculations.calculation import Calculation


class Subtraction(Calculation):
    """ subtracts two numbers """
    def get_result(self):
        """ subtracts two numbers """
        dif_of_vals = 0.0
        for value in self.vals:
            dif_of_vals = dif_of_vals - value
            pprint.pprint(value)
        return dif_of_vals
