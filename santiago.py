from flask import Blueprint, render_template, abort, request
from io import StringIO
import sys
import math
from sympy import evalf, symbols, sympify

from Methods.Python.busquedaIncremental import busqueda
from Methods.Python.biseccion import biseccion
from Methods.Python.reglafalsa import reglafalsa
from Methods.Python.puntofijo import puntofijo
from Methods.Python.newton import newton
from Methods.Python.secante import secante
from Methods.Python.raicesmlt import raicesmlt

from Methods.Python.gausspl import gausspl
from Methods.Python.gausspar import gausspar
from Methods.Python.gausstot import gausstot
from Methods.Python.lusimpl import lusimpl
from Methods.Python.lupar import lupar
from Methods.Python.crout import crout
from Methods.Python.doolittle import doolittle
from Methods.Python.cholesky import cholesky
from Methods.Python.jacobi import jacobi
from Methods.Python.gseidel import gseidel
import numpy as np

santiago = Blueprint('santiago', __name__,
                        template_folder='templates',
                        static_folder='static')

@santiago.route('/')
def show():
    return render_template('singleVariable/incSearch.html')


@santiago.route('/methods/incsearch', methods=['GET', 'POST'])
def incsearch_route():

    def funcion(s):
        x = symbols('x')
        return funct.evalf(subs={x: s})

    if request.method == 'POST':
        function = request.form['function']
        xin = float(request.form['xin'])
        delta = float(request.form['delta'])
        nmax = int(request.form['nmax'])

        try:
            funct = sympify(function)
        except Exception as e:
            print('There was an error with the function ')
            print(e.message, e.args)

        stdout = StringIO()
        sys.stdout = stdout
        x = busqueda(funcion, xin, delta, nmax)
        result_stdout = stdout.getvalue()
        result_stdout = result_stdout.split('\n')
        return render_template('singleVariable/incSearch.html', x=x, stdout=result_stdout)

    return render_template('singleVariable/incSearch.html')


@santiago.route('/methods/bisection', methods=['GET', 'POST'])
def bisection_route():

    def funcion(s):
        x = symbols('x')
        return funct.evalf(subs={x: s})

    if request.method == 'POST':
        function = request.form['function']
        a = float(request.form['a'])
        b = float(request.form['b'])
        nmax = int(request.form['nmax'])
        tol = float(request.form['tol'])

        try:
            funct = sympify(function)
        except Exception as e:
            print('There was an error with the function ')
            print(e.message, e.args)

        stdout = StringIO()
        sys.stdout = stdout
        x = biseccion(funcion, a, b, nmax, tol)
        result_stdout = stdout.getvalue()
        result_stdout = result_stdout.split('\n')
        return render_template('singleVariable/bisection.html', x=x, stdout = result_stdout)
    return render_template('singleVariable/bisection.html')

@santiago.route('/methods/falsepos', methods=['GET', 'POST'])
def falsepos_route():

    def funcion(s):
        x = symbols('x')
        return funct.evalf(subs={x: s})

    if request.method == 'POST':
        f = request.form['function']
        a = float(request.form['a'])
        b = float(request.form['b'])
        nmax = int(request.form['nmax'])
        tol = float(request.form['tol'])

        try:
            funct = sympify(f)
        except Exception as e:
            print('There was an error with the function ')
            print(e.message, e.args)

        stdout = StringIO()
        sys.stdout = stdout
        x = reglafalsa(funcion, a, b, nmax, tol)
        result_stdout = stdout.getvalue()
        result_stdout = result_stdout.split('\n')
        return render_template('singleVariable/falsepos.html', x=x, stdout = result_stdout)
    return render_template('singleVariable/falsepos.html')

@santiago.route('/methods/fixedpoint', methods=['GET', 'POST'])
def fixedpoint_route():
    def funcion(s):
        x = symbols('x')
        return funct.evalf(subs={x: s})

    def fungion(s):
        x = symbols('x')
        return fung.evalf(subs={x: s})

    if request.method == 'POST':
        f = request.form['function']
        g = request.form['fung']
        xini = float(request.form['xini'])
        nmax = int(request.form['nmax'])
        tol = float(request.form['tol'])

        try:
            funct = sympify(f)
        except Exception as e:
            print('There was an error with the function \'f\'')
            print(e.message, e.args)

        try:
            fung = sympify(g)
        except Exception as e:
            print('There was an error with the function \'g\'')
            print(e.message, e.args)

        stdout = StringIO()
        sys.stdout = stdout
        x = puntofijo(funcion, fungion, xini, nmax, tol)
        result_stdout = stdout.getvalue()
        result_stdout = result_stdout.split('\n')
        return render_template('singleVariable/fixedpoint.html', x=x, stdout = result_stdout)
    return render_template('singleVariable/fixedpoint.html')

@santiago.route('/methods/newtonraphs', methods=['GET', 'POST'])
def newtonraphs_route():
    def funcion(s):
        x = symbols('x')
        return funct.evalf(subs={x: s})

    def dfunc(s):
        x = symbols('x')
        return functdx.evalf(subs={x: s})

    if request.method == 'POST':
        f = request.form['function']
        fdx = request.form['fdx']
        xini = float(request.form['xini'])
        nmax = int(request.form['nmax'])
        tol = float(request.form['tol'])

        try:
            funct = sympify(f)
        except Exception as e:
            print('There was an error with the function ')
            print(e.message, e.args)

        try:
            functdx = sympify(fdx)
        except Exception as e:
            print('There was an error with the function\'s derivative ')
            print(e.message, e.args)

        print(type(funct), type(functdx), type(xini), type(nmax), type(tol))
        stdout = StringIO()
        sys.stdout = stdout
        x = newton(funcion, dfunc, xini, nmax, tol)
        result_stdout = stdout.getvalue()
        result_stdout = result_stdout.split('\n')
        return render_template('singleVariable/newtonraphs.html', x=x, stdout = result_stdout)
    return render_template('singleVariable/newtonraphs.html')


@santiago.route('/methods/secant', methods=['GET', 'POST'])
def secant_route():
    def funcion(s):
        x = symbols('x')
        return funct.evalf(subs={x: s})

    if request.method == 'POST':
        f = request.form['function']
        x0 = float(request.form['xin'])
        x1 = float(request.form['x'])
        nmax = int(request.form['nmax'])
        tol = float(request.form['tol'])

        try:
            funct = sympify(f)
        except Exception as e:
            print('There was an error with the function ')
            print(e.message, e.args)

        stdout = StringIO()
        sys.stdout = stdout
        x = secante(funcion, x0, x1, nmax, tol)
        result_stdout = stdout.getvalue()
        result_stdout = result_stdout.split('\n')
        return render_template('singleVariable/secant.html', x=x, stdout = result_stdout)
    return render_template('singleVariable/secant.html')


@santiago.route('/methods/multiroots', methods=['GET', 'POST'])
def multiroots_route():
    def funcion(s):
        x = symbols('x')
        return funct.evalf(subs={x: s})

    def funcdx(s):
        x = symbols('x')
        return fundx.evalf(subs={x: s})

    def func2dx(s):
        x = symbols('x')
        return fun2dx.evalf(subs={x: s})

    if request.method == 'POST':
        f = request.form['function']
        fdx = request.form['fdx']
        f2dx = request.form['fd2x']
        x0 = float(request.form['x0'])
        nmax = int(request.form['nmax'])
        tol = float(request.form['tol'])
        try:
            funct = sympify(f)
        except Exception as e:
            print('There was an error with the function ')
            print(e.message, e.args)

        try:
            fundx = sympify(fdx)
        except Exception as e:
            print('There was an error with the function\'s first derivative')
            print(e.message, e.args)
        try:
            fun2dx = sympify(f2dx)
        except Exception as e:
            print('There was an error with the function\'s second derivative')
            print(e.message, e.args)

        stdout = StringIO()
        sys.stdout = stdout
        x = raicesmlt(funcion, funcdx, func2dx,x0, nmax, tol)
        result_stdout = stdout.getvalue()
        result_stdout = result_stdout.split('\n')
        return render_template('singleVariable/multipleroots.html', x=x, stdout = result_stdout)
    return render_template('singleVariable/multipleroots.html')

@santiago.route('/methods/gausspl/<int:array>', methods=['GET', 'POST'])
def gausspl_route(array):
    data = {}
    data['matrix_size'] = array
    A = np.zeros((array, array))
    b = np.zeros(array)
    if request.method == 'POST':
        for i in range(array):
            for j in range(array):
                A[i][j] =  float(request.form["field"+str(i)+str(j)])

        for i in range(array):
                b[i] =  float(request.form["fieldb"+str(i)])

    stdout  = StringIO()
    sys.stdout = stdout # Output will be recorded
    x = gausspl(A, b)
    result_stdout = stdout.getvalue()
    result_stdout = result_stdout.split('\n')
    return render_template('Linear/gausspl.html', x = x, stdout = result_stdout, data = data)

@santiago.route('/methods/gausspar/<int:array>', methods=['GET', 'POST'])
def gausspar_route(array):
    data = {}
    data['matrix_size'] = array
    A = np.zeros((array, array))
    b = np.zeros(array)
    if request.method == 'POST':
        for i in range(array):
            for j in range(array):
                A[i][j] =  float(request.form["field"+str(i)+str(j)])

        for i in range(array):
                b[i] =  float(request.form["fieldb"+str(i)])

    stdout  = StringIO()
    sys.stdout = stdout # Output will be recorded
    x = gausspar(A, b)
    result_stdout = stdout.getvalue()
    result_stdout = result_stdout.split('\n')
    return render_template('Linear/gausspar.html', x = x, stdout = result_stdout, data = data)

@santiago.route('/methods/gausstot/<int:array>', methods=['GET', 'POST'])
def gausstot_route(array):
    data = {}
    data['matrix_size'] = array
    A = np.zeros((array, array))
    b = np.zeros(array)
    if request.method == 'POST':
        for i in range(array):
            for j in range(array):
                A[i][j] =  float(request.form["field"+str(i)+str(j)])

        for i in range(array):
                b[i] =  float(request.form["fieldb"+str(i)])

    stdout  = StringIO()
    sys.stdout = stdout # Output will be recorded
    x = gausstot(A, b)
    result_stdout = stdout.getvalue()
    result_stdout = result_stdout.split('\n')
    return render_template('Linear/gausstot.html', x = x, stdout = result_stdout, data = data)

@santiago.route('/methods/lusimpl/<int:array>', methods=['GET', 'POST'])
def lusimpl_route(array):
    data = {}
    data['matrix_size'] = array
    A = np.zeros((array, array))
    b = np.zeros(array)
    if request.method == 'POST':
        for i in range(array):
            for j in range(array):
                A[i][j] =  float(request.form["field"+str(i)+str(j)])

        for i in range(array):
                b[i] =  float(request.form["fieldb"+str(i)])

    stdout  = StringIO()
    sys.stdout = stdout # Output will be recorded
    x = lusimpl(A, b)
    result_stdout = stdout.getvalue()
    result_stdout = result_stdout.split('\n')
    return render_template('Linear/lusimpl.html', x = x, stdout = result_stdout, data = data)

@santiago.route('/methods/lupar/<int:array>', methods=['GET', 'POST'])
def lupar_route(array):
    data = {}
    data['matrix_size'] = array
    A = np.zeros((array, array))
    b = np.zeros(array)
    if request.method == 'POST':
        for i in range(array):
            for j in range(array):
                A[i][j] =  float(request.form["field"+str(i)+str(j)])

        for i in range(array):
                b[i] =  float(request.form["fieldb"+str(i)])

    stdout  = StringIO()
    sys.stdout = stdout # Output will be recorded
    x = lupar(A, b)
    result_stdout = stdout.getvalue()
    result_stdout = result_stdout.split('\n')
    return render_template('Linear/lupar.html', x = x, stdout = result_stdout, data = data)

@santiago.route('/methods/crout/<int:array>', methods=['GET', 'POST'])
def crout_route(array):
    data = {}
    data['matrix_size'] = array
    A = np.zeros((array, array))
    b = np.zeros(array)
    if request.method == 'POST':
        for i in range(array):
            for j in range(array):
                A[i][j] =  float(request.form["field"+str(i)+str(j)])

        for i in range(array):
                b[i] =  float(request.form["fieldb"+str(i)])

    stdout  = StringIO()
    sys.stdout = stdout # Output will be recorded
    x = crout(A, b)
    result_stdout = stdout.getvalue()
    result_stdout = result_stdout.split('\n')
    return render_template('Linear/crout.html', x = x, stdout = result_stdout, data = data)

@santiago.route('/methods/doolittle/<int:array>', methods=['GET', 'POST'])
def doolittle_route(array):
    data = {}
    data['matrix_size'] = array
    A = np.zeros((array, array))
    b = np.zeros(array)
    if request.method == 'POST':
        for i in range(array):
            for j in range(array):
                A[i][j] =  float(request.form["field"+str(i)+str(j)])

        for i in range(array):
                b[i] =  float(request.form["fieldb"+str(i)])

    stdout  = StringIO()
    sys.stdout = stdout # Output will be recorded
    x = doolittle(A, b)
    result_stdout = stdout.getvalue()
    result_stdout = result_stdout.split('\n')
    return render_template('Linear/doolittle.html', x = x, stdout = result_stdout, data = data)

@santiago.route('/methods/cholesky/<int:array>', methods=['GET', 'POST'])
def cholesky_route(array):
    data = {}
    data['matrix_size'] = array
    A = np.zeros((array, array))
    b = np.zeros(array)
    if request.method == 'POST':
        for i in range(array):
            for j in range(array):
                A[i][j] =  float(request.form["field"+str(i)+str(j)])

        for i in range(array):
                b[i] =  float(request.form["fieldb"+str(i)])

    stdout  = StringIO()
    sys.stdout = stdout # Output will be recorded
    x = cholesky(A, b)
    result_stdout = stdout.getvalue()
    result_stdout = result_stdout.split('\n')
    return render_template('Linear/cholesky.html', x = x, stdout = result_stdout, data = data)

@santiago.route('/methods/jacobi/<int:array>', methods=['GET', 'POST'])
def jacobi_route(array):
    data = {}
    data['matrix_size'] = array
    A = np.zeros((array, array))
    b = np.zeros(array)
    x0 = np.zeros(array)
    tol = 0
    nmax = 0
    if request.method == 'POST':
        nmax = float(request.form["fieldNmax"])
        tol = float(request.form["fieldTol"])
        for i in range(array):
            for j in range(array):
                A[i][j] =  float(request.form["field"+str(i)+str(j)])

        for i in range(array):
            b[i] = float(request.form["fieldb"+str(i)])

        for i in range(array):
            x0[i] = float(request.form["fieldx"+str(i)])

    stdout  = StringIO()
    sys.stdout = stdout # Output will be recorded
    x = jacobi(A, b, x0, tol, nmax)
    result_stdout = stdout.getvalue()
    result_stdout = result_stdout.split('\n')
    return render_template('Linear/jacobi.html', x = x, stdout = result_stdout, data = data)

@santiago.route('/methods/gseidel/<int:array>', methods=['GET', 'POST'])
def gseidel_route(array):
    data = {}
    data['matrix_size'] = array
    A = np.zeros((array, array))
    b = np.zeros(array)
    x0 = np.zeros(array)
    tol = 0
    nmax = 0
    if request.method == 'POST':
        nmax = float(request.form["fieldNmax"])
        tol = float(request.form["fieldTol"])
        for i in range(array):
            for j in range(array):
                A[i][j] =  float(request.form["field"+str(i)+str(j)])

        for i in range(array):
            b[i] = float(request.form["fieldb"+str(i)])

        for i in range(array):
            x0[i] = float(request.form["fieldx"+str(i)])

    stdout  = StringIO()
    sys.stdout = stdout # Output will be recorded
    x = gseidel(A, b, x0, tol, nmax)
    result_stdout = stdout.getvalue()
    result_stdout = result_stdout.split('\n')
    return render_template('Linear/gseidel.html', x = x, stdout = result_stdout, data = data)

def matrix_str(A):
    mstr = ''
    n = A.shape[0]
    for i in range(n):
        for j in range(n):
            mstr += "{number: .3f}".format(number = A[i][j])
        mstr += '\n'

    return mstr
