""" multiplies two numbers """
from individual_calc.calculation import Calculation


class Multiplication(Calculation):
    """ multiplies two numbers """
    def get_result(self):
        """ multiplies two numbers """
        return self.val_a * self.val_b
