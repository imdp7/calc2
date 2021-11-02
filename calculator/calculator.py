""" This is the increment function"""
class Calculator:
    """ This is the Calculator class"""
    history = []
    result = 0

    @staticmethod
    def add_number(val_a, val_b):
        """ adds number to result"""
        return val_a + val_b

    @staticmethod
    def subtract_number(val_a, val_b):
        """ subtract number from result"""
        return val_a - val_b

    @staticmethod
    def multiply_numbers(val_a, val_b):
        """ multiply two numbers and store the result"""
        return val_a * val_b

    @staticmethod
    def divide_numbers(val_a, val_b):
        """divide two numbers and store the result"""
        return val_a / val_b

    def get_result(self):
        """ return the result of a calculation """
        return self.result
