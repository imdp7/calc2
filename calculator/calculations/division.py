""" divides two numbers """
from calculator.calculations.calculation import Calculation


class Division(Calculation):
    """ divides two numbers """
    def get_result(self):
        """ divides two numbers """
        division_values = self.values[0]
        # print(type(float(div_values)))
        for value in self.values[1:]:
            try:
                division_values = float(division_values) / float(value)
            except ZeroDivisionError:
                return "Error"
        return division_values
