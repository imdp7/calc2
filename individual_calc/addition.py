""" adds two numbers """
from individual_calc.calculation import Calculation

class Addition(Calculation):
    """ adds two numbers """
    def get_result(self):
        """ adds two numbers """
        return self.val_a + self.val_b
