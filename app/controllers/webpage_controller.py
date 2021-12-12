""" Webpage Controller """
# pylint: disable=no-name-in-module, import-error, too-few-public-methods
from flask import render_template
from app.controllers.controller import ControllerBase


class AboutController(ControllerBase):
    """ Webpage Controller """
    @staticmethod
    def get():
        """ Webpage Controller """
        return render_template('about.html')


class AAAController(ControllerBase):
    """ Webpage Controller """
    @staticmethod
    def get():
        """ Webpage Controller """
        return render_template('aaatesting.html')


class PIEAController(ControllerBase):
    """ Webpage Controller """
    @staticmethod
    def get():
        """ Webpage Controller """
        return render_template('pieacalculator.html')


class SeparationOfConcernsController(ControllerBase):
    """ Webpage Controller """
    @staticmethod
    def get():
        """ Webpage Controller """
        return render_template('separationofconcerns.html')


class TipsAndTricksController(ControllerBase):
    """ Webpage Controller """
    @staticmethod
    def get():
        """ Webpage Controller """
        return render_template('tipsandtricks.html')
