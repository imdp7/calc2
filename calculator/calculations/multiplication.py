""" multiplies two numbers """
from calculator.calculations.calculation import Calculation


class Multiplication(Calculation):
    """ multiplies two numbers """
    def get_result(self):
        """ multiplies two numbers """
        result = 1.0
        for value in self.vals:
            result = result * value
        return result
