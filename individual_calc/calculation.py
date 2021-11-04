""" sets up the program to perform calculations """
class Calculation: # pylint: disable=too-few-public-methods
    """ constructor, first function called """
    def __init__(self, val_a, val_b):
        self.val_a = val_a
        self.val_b = val_b

    @classmethod
    def create(cls, val_a, val_b):
        """ class factory method """
        return cls(val_a, val_b)
