from flask import Blueprint, render_template, request
from io import StringIO
import sys
import numpy as np


# Import the methods
from Methods.Python.vandermonde import vandermonde
from Methods.Python.difdivididas import difdivididas # Newton
from Methods.Python.lagrange import lagrange
from Methods.Python.trazlin import trazlin
from Methods.Python.trazcuad import trazcuad
from Methods.Python.trazcub import trazcub

urrego = Blueprint('urrego', __name__,
                        template_folder='templates',
                        static_folder='static')

@urrego.route('/methods/vandermonde/<int:array>', methods=['GET','POST'])
def vandermonde_route(array):
    data = {}
    data['title'] = 'Vandermonde'
    result_stdout = None
    if request.method == 'POST':
        X = []
        Y = []
        for n in range(array):
            X.append(float(request.form["field0"+str(n)]))
            Y.append(float(request.form["field1"+str(n)]))
        stdout  = StringIO()
        sys.stdout = stdout
        vandermonde(np.array(X),np.array(Y))
        result_stdout = stdout.getvalue()
        result_stdout = result_stdout.strip().split('\n')
        data['summary'] = result_stdout
        sys.stdout.close()


    # Configuration of the input array
    data['message'] = ''
    if array < 1:
        array = 1
        data['message'] = "The array can't be less than zero"
    elif array > 11:
        array = 11
        data['message'] = "The array can't be more than 11"    
    data['array_len'] = array
    
    return render_template('interpolation/vandermonde.html', data = data)

@urrego.route('/methods/newton/<int:array>', methods=['GET','POST'])
def newton_interpolation_route(array):
    data = {}
    data['title'] = 'Newton'

    if request.method == 'POST':
        X = []
        Y = []
        for n in range(array):
            X.append(float(request.form["field0"+str(n)]))
            Y.append(float(request.form["field1"+str(n)]))
        stdout  = StringIO()
        sys.stdout = stdout
        difdivididas(np.array(X),np.array(Y))
        result_stdout = stdout.getvalue()
        result_stdout = result_stdout.split('\n')
        data['summary'] = result_stdout
        stdout.close()

    # Configuration of the input array
    data['message'] = ''
    if array < 1:
        array = 1
        data['message'] = "The array can't be less than zero"
    elif array > 11:
        array = 11
        data['message'] = "The array can't be more than 11"    
    data['array_len'] = array

    return render_template('interpolation/newton.html', data = data)

@urrego.route('/methods/lagrange/<int:array>', methods=['GET','POST'])
def lagrange_route(array):
    data = {}
    data['title'] = 'Lagrange'
    
    if request.method == 'POST':
        X = []
        Y = []
        for n in range(array):
            X.append(float(request.form["field0"+str(n)]))
            Y.append(float(request.form["field1"+str(n)]))
        stdout  = StringIO()
        sys.stdout = stdout
        lagrange(np.array(X),np.array(Y))
        result_stdout = stdout.getvalue()
        result_stdout = result_stdout.split('\n')
        data['summary'] = result_stdout
        stdout.close()

    # Configuration of the input array
    data['message'] = ''
    if array < 1:
        array = 1
        data['message'] = "The array can't be less than zero"
    elif array > 11:
        array = 11
        data['message'] = "The array can't be more than 11"    
    data['array_len'] = array
    
    return render_template('interpolation/lagrange.html', data = data)

@urrego.route('/methods/spline_linear/<int:array>', methods=['GET','POST'])
def spline_linear_route(array):
    data = {}
    data['title'] = 'Spline Linear'
    
    if request.method == 'POST':
        X = []
        Y = []
        for n in range(array):
            X.append(float(request.form["field0"+str(n)]))
            Y.append(float(request.form["field1"+str(n)]))
        stdout  = StringIO()
        sys.stdout = stdout
        trazlin(np.array(X),np.array(Y))
        result_stdout = stdout.getvalue()
        result_stdout = result_stdout.split('\n')
        data['summary'] = result_stdout
        stdout.close()

    # Configuration of the input array
    data['message'] = ''
    if array < 1:
        array = 1
        data['message'] = "The array can't be less than zero"
    elif array > 11:
        array = 11
        data['message'] = "The array can't be more than 11"    
    data['array_len'] = array
    
    return render_template('interpolation/spline_linear.html', data = data)

@urrego.route('/methods/spline_square/<int:array>', methods=['GET','POST'])
def spline_square_route(array):
    data = {}
    data['title'] = 'Spline Square'
    
    if request.method == 'POST':
        X = []
        Y = []
        for n in range(array):
            X.append(float(request.form["field0"+str(n)]))
            Y.append(float(request.form["field1"+str(n)]))
        stdout  = StringIO()
        sys.stdout = stdout
        trazcuad(np.array(X),np.array(Y))
        result_stdout = stdout.getvalue()
        result_stdout = result_stdout.split('\n')
        data['summary'] = result_stdout
        stdout.close()

    # Configuration of the input array
    data['message'] = ''
    if array < 1:
        array = 1
        data['message'] = "The array can't be less than zero"
    elif array > 11:
        array = 11
        data['message'] = "The array can't be more than 11"    
    data['array_len'] = array
    
    return render_template('interpolation/spline_square.html', data = data)

@urrego.route('/methods/spline_cubica/<int:array>', methods=['GET','POST'])
def spline_cubic_route(array):
    data = {}
    data['title'] = 'Spline Cubic'
    
    if request.method == 'POST':
        X = []
        Y = []
        for n in range(array):
            X.append(float(request.form["field0"+str(n)]))
            Y.append(float(request.form["field1"+str(n)]))
        stdout  = StringIO()
        sys.stdout = stdout
        trazcub(np.array(X),np.array(Y))
        result_stdout = stdout.getvalue()
        result_stdout = result_stdout.split('\n')
        data['summary'] = result_stdout
        stdout.close()

    # Configuration of the input array
    data['message'] = ''
    if array < 1:
        array = 1
        data['message'] = "The array can't be less than zero"
    elif array > 11:
        array = 11
        data['message'] = "The array can't be more than 11"    
    data['array_len'] = array
    
    return render_template('interpolation/spline_cubic.html', data = data)
