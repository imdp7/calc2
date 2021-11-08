""" sets up the program to perform calculations """
class Calculation: # pylint: disable=too-few-public-methods
    """ constructor, first function called """
    def __init__(self,vals: tuple):
        self.vals = Calculation.convert_args_to_list_float(vals)

    @staticmethod
    def convert_args_to_list_float(vals):
        """ make a list of floats """
        list_vals_float = []
        for element in vals:
            list_vals_float.append(float(element))
        return list_vals_float
