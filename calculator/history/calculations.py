""" Calculation History Class """
class Calculation:
    """ Calculation History Class """
    history = []
    # pylint: disable=too-few-public-methods
    @staticmethod
    def empty_history():
        """ clears history function """
        Calculation.history.clear()
        return True


    @staticmethod
    def add_to_history(calculation):
        """ adds the calculation to history when called """
        return Calculation.history.append(calculation)


    @staticmethod
    def history_count():
        """ however many calculations have been stored in the array """
        return len(Calculation.history)


    @staticmethod
    def get_calculation(num):
        """ calling the previous calculation """
        return Calculation.history[num]


    @staticmethod
    def last_calc_to_history():
        """ returns the last calc in the array """
        return Calculation.history[-1]


    @staticmethod
    def first_calc_to_history():
        """ adds the first calculation to history """
        return Calculation.history[0]
