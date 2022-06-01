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

alejandro = Blueprint('alejandro', __name__,
                        template_folder='templates',
                        static_folder='static')

@alejandro.route('/')
def show():
    return render_template('singleVariable/incSearch.html')


@alejandro.route('/methods/incsearch', methods=['GET', 'POST'])
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


@alejandro.route('/methods/bisection', methods=['GET', 'POST'])
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

@alejandro.route('/methods/falsepos', methods=['GET', 'POST'])
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

@alejandro.route('/methods/fixedpoint', methods=['GET', 'POST'])
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

@alejandro.route('/methods/newtonraphs', methods=['GET', 'POST'])
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


@alejandro.route('/methods/secant', methods=['GET', 'POST'])
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


@alejandro.route('/methods/multiroots', methods=['GET', 'POST'])
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

