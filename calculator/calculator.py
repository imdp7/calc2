""" This is the increment function"""
class Calculator:
    """ This is the Calculator class"""
    history = []
    result = 0

    @staticmethod
    def add_number(a, b):
        """ adds number to result"""
        return a + b

    @staticmethod
    def subtract_number(a, b):
        """ subtract number from result"""
        return a - b

    @staticmethod
    def multiply_numbers(a, b):
        """ multiply two numbers and store the result"""
        return a * b

    @staticmethod
    def divide_numbers(a,b):
        """divide two numbers and store the result"""
        return a / b

    @staticmethod
    def get_result(result):
        return result
