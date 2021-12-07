"""A simple flask web app"""
from flask import Flask, request
from flask import render_template
from calculator.calculator import Calculator
app = Flask(__name__)

@app.route("/")
def index():
    """index  Route Response"""
    return render_template('index.html')

@app.route("/basicform", methods=['GET', 'POST'])
def basicform():
    """Post Request Handling"""
    if request.method == 'POST':
        #get the values out of the form
        valuea = request.form['valuea']
        valueb = request.form['valueb']
        sign = request.form['sign']
        #make the tuple
        my_tuple = (valuea, valueb)
        #this will call the correct operation
        getattr(Calculator, sign)(my_tuple)
        valuec = str(Calculator.get_last_calculation())
        return render_template('result.html', valuea=valuea, valueb=valueb, sign=sign, valuec=valuec)
    # Displays the form because if it isn't a post it is a get request
    else:
        return render_template('basicform.html')


@app.route("/bad/<value1>/<value2>")
def bad_calc(valuea, valueb):
    """bad calc Route Response"""
    result = valuea + valueb
    response = "The result of the calculation is: " + result + '<a href="/"> back</a>'
    return response

@app.route("/good/<float:value1>/<float:value2>")
def good_calc(value1, value2):
    """good calc Route Response"""
    my_tuple = (value1, value2)
    Calculator.addition(my_tuple)
    response = "The result of the calculation is: " + str(Calculator.get_last_result_value()) + '<a href="/"> back</a>'
    return response
