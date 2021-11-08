""" This is the increment function"""
from calculator.calculations.addition import Addition
from calculator.calculations.subtraction import Subtraction
from calculator.calculations.multiplication import Multiplication
from calculator.calculations.division import Division
from calculator.history.calculations import Calculation


class Calculator:
    """ This is the Calculator class"""

    @staticmethod
    def add_number(*args):
        """ adds number to result"""
        calculation = Addition(args)
        Calculation.add_to_history(calculation)
        return calculation.get_result()

    @staticmethod
    def subtract_number(*args):
        """ subtract number from result"""
        calculation = Subtraction(args)
        Calculation.add_to_history(calculation)
        return calculation.get_result()

    @staticmethod
    def multiply_numbers(*args):
        """ multiply two numbers and store the result"""
        calculation = Multiplication(args)
        Calculation.add_to_history(calculation)
        return calculation.get_result()

    @staticmethod
    def divide_numbers(*args):
        """divide two numbers and store the result"""
        calculation = Division(args)
        Calculation.add_to_history(calculation)
        return calculation.get_result()
