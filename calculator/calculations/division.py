""" divides two numbers """
from calculator.calculations.calculation import Calculation


class Division(Calculation):
    """ divides two numbers """
    def get_result(self):
        """ divides two numbers """
        result = 1.0
        for value in self.vals:
            result = value / result
        return result
