""" subtracts two numbers """
from individual_calc.calculation import Calculation


class Subtraction(Calculation):
    """ subtracts two numbers """
    def get_result(self):
        """ subtracts two numbers """
        return self.val_a - self.val_b
