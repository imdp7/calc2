""" divides two numbers """
from individual_calc.calculation import Calculation


class Division(Calculation):
    """ divides two numbers """
    def get_result(self):
        """ divides two numbers """
        return self.val_a / self.val_b
