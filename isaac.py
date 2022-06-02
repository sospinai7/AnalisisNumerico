from crypt import methods
from flask import Blueprint, render_template, request, abort
from io import StringIO
import sys
import numpy as np

# Import the methods
from Methods.Python.vandermonde import vandermonde
from Methods.Python.difdivididas import difdivididas # Newton
from Methods.Python.lagrange import lagrange
from Methods.Python.trazlin import trazlin
from Methods.Python.trazcuad import trazcuad

history = []

isaac = Blueprint('isaac', __name__,
                           template_folder='templates',
                           static_folder='static')

@isaac.route('/form')
def show():
    return render_template('index.html')

@isaac.route('isaac/form', methods=['POST', 'GET'])
def form():
    fx = request.form.get('fx')
    a = request.form.get('a')
    b = request.form.get('b')
    history.append(f'{fx}')
    title = 'graph'
    return render_template('graph/form.html', title = title, history = history, fx = fx, a = a, b = b)

@isaac.route('/form' , methods=["POST", "GET"])
def form2():
    fx = request.form.get('fx')
    a=request.form.get("a")
    b=request.form.get("b")
    history.append(f"{fx}")
    title= "graph"
    return render_template("graph/form.html", title=title, history= history, fx=fx, a=a, b=b)

@isaac.route('/graph' , methods=["POST", "GET"])
def graph():
    data = {'title':'Function Plotter'}
    return render_template('graph/graph.html', data = data)

@isaac.route('isaac/help')
def help_route2():
    return render_template("nav/help.html")

#methods 
@isaac.route('/methods/vandermonde/<int:array>', methods=['GET','POST'])
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


@isaac.route('/methods/newton/<int:array>', methods=['GET','POST'])
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


@isaac.route('/methods/lagrange/<int:array>', methods=['GET','POST'])
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


@isaac.route('/methods/spline_linear/<int:array>', methods=['GET','POST'])
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


@isaac.route('/methods/spline_square/<int:array>', methods=['GET','POST'])
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


