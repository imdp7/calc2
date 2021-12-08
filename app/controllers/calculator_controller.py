from app.controllers.controller import ControllerBase
from calculator.calculator import Calculator
from flask import render_template, request, flash, redirect, url_for


class CalculatorController(ControllerBase):
    @staticmethod
    def post():
        if request.form['valuea'] == '' or request.form['valueb'] == '':
            error = 'You need at least one value filled out, try again!'
        else:
            flash('flashed message')
            # get the values out of the form
            valuea = request.form['valuea']
            valueb = request.form['valueb']
            operation = request.form['operation']
            # make the tuple
            my_tuple = (valuea, valueb)
            # this will call the correct operation
            getattr(Calculator, operation)(my_tuple)
            valuec = str(Calculator.get_last_calculation())
            return render_template('result.html', valuea=valuea, valueb=valueb, operation=operation, valuec=valuec)

        return render_template('calculator2.html', error=error)
    @staticmethod
    def get():
        return render_template('calculator2.html')
