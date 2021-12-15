""" This is the increment function"""
from calculator.calculations.addition import Addition
from calculator.calculations.subtraction import Subtraction
from calculator.calculations.multiplication import Multiplication
from calculator.history.calculations import Calculations
from calculator.calculations.division import Division

class Calculator:
    """ This is the Calculator class"""
    @staticmethod
    def add_numbers(*args):
        """ adds list of numbers"""
        calculation = Addition(args)
        Calculations.add_calculation(calculation)
        return calculation.get_result()
    @staticmethod
    def subtract_numbers(*args):
        """ subtract a list of numbers from result"""
        calculation = Subtraction(args)
        Calculations.add_calculation(calculation)
        return calculation.get_result()
    @staticmethod
    def multiply_numbers(*args):
        """ multiplication number from result"""
        calculation = Multiplication(args)
        Calculations.add_calculation(calculation)
        return calculation.get_result()
    @staticmethod
    def divide_numbers(*args):
        """ Division number from result"""
        calculation = Division(args)
        Calculations.add_calculation(calculation)

        return calculation.get_result()
