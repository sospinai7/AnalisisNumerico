""" 
Python Code: Fixed Point
An Fixed Point method implementation
"""

from sympy import var
from sympy import sympify
import customTools as ct


def fixed_point(exp, g_exp, x0, t_error, imax, tol):
    '''
    Parameters:
    :exp: function to evaluate
    :g_exp: derivative of the function (exp)
    :x0: x initial value
    :t_error: kind of error to work with
    :imax: max limit of iterations
    :tol: tolerance
    '''
    x = var('x')
    f = sympify(exp)
    g = sympify(g_exp)
    fx = f.subs(x, x0)
    result = []
    i = 1
    error = tol+1
    result.append([i,x0,fx,error])
    
    while fx != 0 and error > tol and i <= imax:
        x1 = g.subs(x, x0)
        fx = f.subs(x, x1)
        if t_error == 1:
            error = abs(x1-x0)
        else:
            error = abs((x1-x0)/x1)
        x0 = x1
        i += 1
        result.append([i,x0,fx,error])
        
    ct.imprimir(['Iteración', 'x', 'f(x)', 'Error'], result)
    if fx == 0:
        print(x0, ' es una raíz')
    elif error <= tol:
        print(x0, ' se aproxima a una raíz con una tolerancia de ', tol)
    else:
        print('Se llegó al límite de iteraciones')
        