from sympy import var
from sympy import sympify
import customTools as ct

def falsePosition(x0,x1,e,fx):
    step = 1

    condicion = True
    while condicion:
        x2 = x0 - (x1-x0) * ct.f(x0, fx)/( ct.f(x1, fx) - ct.f(x0, fx) )
        #print('Iteracion-%d, x2 = %0.6f y f(x2) = %0.6f' % (step, x2, f(x2)))

        if ct.f(x0, fx) * ct.f(x2, fx) < 0:
            x1 = x2
        else:
            x0 = x2

        step = step + 1
        condicion = abs(ct.f(x2, fx)) > e

    print('\nRaiz: %0.8f' % x2)

x0 = float(input('x0: '))
x1 = float(input('x1: '))
e = float(input('Toleracia: '))
fx = input('Funcion: ')


if ct.f(x0, fx) * ct.f(x1, fx) > 0.0:
    print('Intenta otros valores')
else:
    falsePosition(x0,x1,e,fx)
