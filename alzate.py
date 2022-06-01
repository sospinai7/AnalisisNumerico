from flask import Blueprint, render_template, abort, request
from io import StringIO
import sys

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
from Methods.Python.sor import sor
import numpy as np

alzate = Blueprint('alzate', __name__,
                        template_folder='templates',
                        static_folder='static')

@alzate.route('/')
def show():
    return render_template('Linear/gausspl.html')

@alzate.route('/methods/gausspl/<int:array>', methods=['GET', 'POST'])
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

@alzate.route('/methods/gausspar/<int:array>', methods=['GET', 'POST'])
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

@alzate.route('/methods/gausstot/<int:array>', methods=['GET', 'POST'])
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

@alzate.route('/methods/lusimpl/<int:array>', methods=['GET', 'POST'])
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

@alzate.route('/methods/lupar/<int:array>', methods=['GET', 'POST'])
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

@alzate.route('/methods/crout/<int:array>', methods=['GET', 'POST'])
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

@alzate.route('/methods/doolittle/<int:array>', methods=['GET', 'POST'])
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

@alzate.route('/methods/cholesky/<int:array>', methods=['GET', 'POST'])
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

@alzate.route('/methods/jacobi/<int:array>', methods=['GET', 'POST'])
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

@alzate.route('/methods/gseidel/<int:array>', methods=['GET', 'POST'])
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

@alzate.route('/methods/sor/<int:array>', methods=['GET', 'POST'])
def sor_route(array):
    data = {}
    data['matrix_size'] = array
    A = np.zeros((array, array))
    b = np.zeros(array)
    x0 = np.zeros(array)
    tol = 0
    nmax = 0
    w = 0
    if request.method == 'POST':
        nmax = float(request.form["fieldNmax"])
        tol = float(request.form["fieldTol"])
        w = float(request.form["fieldw"])
        for i in range(array):
            for j in range(array):
                A[i][j] =  float(request.form["field"+str(i)+str(j)])

        for i in range(array):
            b[i] = float(request.form["fieldb"+str(i)])

        for i in range(array):
            x0[i] = float(request.form["fieldx"+str(i)])

    stdout  = StringIO()
    sys.stdout = stdout # Output will be recorded
    x = sor(A, b, x0, w, tol, nmax)
    result_stdout = stdout.getvalue()
    result_stdout = result_stdout.split('\n')
    return render_template('Linear/sor.html', x = x, stdout = result_stdout, data = data)

def matrix_str(A):
    mstr = ''
    n = A.shape[0]
    for i in range(n):
        for j in range(n):
            mstr += "{number: .3f}".format(number = A[i][j])
        mstr += '\n'

    return mstr
