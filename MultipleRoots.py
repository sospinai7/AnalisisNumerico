# import sympy as sp
from sympy import var
from sympy import sympify
from sympy import *
import math
from math import *

x= symbols('x')

def multipleRoots(fx, x0, maxI, tol):
    fx = parse_expr(fx)
    ux= fx/diff(fx)
    uxx= diff(ux)
    cont=0
    error= tol+1

    while cont<maxI and error>tol:
        xn= x0-ux.subs(x,x0)/uxx.subs(x,x0)
        error= abs(xn-x0)
        cont= cont+1
        x0=xn

    if error<=tol:
        return 'Raiz: ' + str(xn) + ', en la iteracion: ' + str(cont-1)
        
    else:
        return 'No converge'

print(multipleRoots('x*2.71828182**(x)-2.71828182**(x)+1', 0.5, 10, 0.00001))