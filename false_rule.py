from sympy import var
from sympy import sympify
import customTools as ct
from sympy import *
import math
from math import *

x = symbols('x')

def f(x, funcion):
    incognita = var('x')
    user_input = funcion # 'x**3-5*x-9'
    expr = sympify(user_input)
    resultado = expr.subs(incognita, x)
    return resultado

def falsePosition(x0,x1,e,fx,maxI):
    fx = parse_expr(fx)
    step = 0
    condicion = True

    if fx.subs(x,x0)*fx.subs(x,x1)==0:
        return str(x0) + ' o ' + str(x1) + ' son raiz'
    elif fx.subs(x,x0)*fx.subs(x,x1)>0:
        return 'No hay raiz'
    else:
        xm= x1- fx.subs(x,x1)*(x0-x1)/(fx.subs(x,x0)-fx.subs(x,x1))
        step=0
        error= abs(x0-xm)

    while condicion:
        x2 = x0 - (x1-x0) * ct.f(x0, fx)/( ct.f(x1, fx) - ct.f(x0, fx) )
        #print('Iteracion-%d, x2 = %0.6f y f(x2) = %0.6f' % (step, x2, f(x2)))

        if ct.f(x0, fx) * ct.f(x2, fx) < 0:
            x1 = x2
        else:
            x0 = x2

        xm = x1- fx.subs(x,x1)*(x0-x1)/(fx.subs(x,x0)-fx.subs(x,x1))
        error = abs(x0-xm)    
        step = step + 1
        condicion = abs(f(x2, fx)) > e and maxI>step and fx.subs(x,xm)!=0

    if fx.subs(x, xm) == 0:
      return str(xm) + ' es raiz'
    elif error < e:
      return str(xm) + ' es raiz con tolerancia ' + str(e)

    print('\nRaiz: %0.8f' % x2)

x0 = float(input('x0: '))
x1 = float(input('x1: '))
e = float(input('Toleracia: '))
maxI = float(input('Iteraiciones Maximas: '))
fx = input('Funcion: ')


if ct.f(x0, fx) * ct.f(x1, fx) > 0.0:
    print('Intenta otros valores')
else:
    falsePosition(x0,x1,e,fx,maxI)
