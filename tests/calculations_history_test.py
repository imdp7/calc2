""" Testing Calculator """
import pytest
from calculator.history.calculations import Calculation
from calculator.calculations.addition import Addition

@pytest.fixture
def clear_history_fixture():
    """ Clears history after each run """
    Calculation.empty_history()
@pytest.fixture
def setup_addition_calc_fixture():
    """ Runs each time a test is passed through it """
    # pylint: disable=redefined-outer-name
    values = (5, 4)
    addition = Addition(values)
    Calculation.add_to_history(addition)

def add_calc_to_history_test(clear_history_fixture, setup_addition_calc_fixture):
    """ Testing if clear history returns true """
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert Calculation.history_count() == 1

def clear_history_calculation_test(clear_history_fixture, setup_addition_calc_fixture):
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    """ testing if history can be cleared """
    assert Calculation.history_count() == 1
    Calculation.empty_history()
    assert Calculation.history_count() == 0
    assert Calculation.empty_history() == True

def get_calculation_test(clear_history_fixture, setup_addition_calc_fixture):
    """ Testing if it is possible to get a specific calculation from the history """
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculation.get_calculation(0).get_result() == 3

def get_last_calculation_test(clear_history_fixture, setup_addition_calc_fixture):
    """ testing obtaining the last calculation from history """
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculation.last_calc_to_history().get_result() == 3

def get_first_calculation_test(clear_history_fixture, setup_addition_calc_fixture):
    """ testing obtaining the first calculation from history """
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculation.first_calc_to_history().get_result() == 3

def history_count_test():
    """ testing if history is tracking calculations """
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculation.history_count() == 1
