""" A simple flask web app """
# pylint: disable=no-name-in-module, import-error
import sys
import os
from flask import Flask, request

from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from app.controllers.data_table_controller import DataTableController
from app.controllers.webpage_controller import AboutController, AAAController, PIEAController, \
    SeparationOfConcernsController, TipsAndTricksController


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


parent_dir = os.getcwd()
path = os.path.dirname(parent_dir)
sys.path.append(parent_dir)


@app.route("/", methods=['GET'])
def index_get():
    """ Returns index """
    return IndexController.get()


@app.route("/calculator", methods=['GET'])
def calculator_get():
    """ Returns calculator """
    return CalculatorController.get()


@app.route("/calculator", methods=['POST'])
def calculator_post():
    """ Returns calculator results """
    return CalculatorController.post()


@app.route("/data_table", methods=['GET', 'POST'])
def data_table():
    """ Results Table Route """
    if request.method == 'POST':
        return DataTableController.post()
    return DataTableController.get()


@app.route("/about", methods=['GET'])
def about_get():
    """ Returns about """
    return AboutController.get()


@app.route("/aaatesting", methods=['GET'])
def aaatesting_get():
    """ returns aaa testing """
    return AAAController.get()


@app.route("/pieacalculator", methods=['GET'])
def pieacalculator_get():
    """ returns pieacalc """
    return PIEAController.get()


@app.route("/separationofconcerns", methods=['GET'])
def separationofconcerns_get():
    """ returns separation of concerns """
    return SeparationOfConcernsController.get()


@app.route("/tipsandtricks", methods=['GET'])
def tipsandtricks_get():
    """ returns tips and tricks """
    return TipsAndTricksController.get()
