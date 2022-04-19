from sympy import var
from sympy import sympify

def f(x, funcion):
    incognita = var('x')
    user_input = funcion # 'x**3-5*x-9'
    expr = sympify(user_input)
    resultado = expr.subs(incognita, x)
    return resultado

def falsePosition(x0,x1,e,fx):
    step = 1

    condicion = True
    while condicion:
        x2 = x0 - (x1-x0) * f(x0, fx)/( f(x1, fx) - f(x0, fx) )
        #print('Iteracion-%d, x2 = %0.6f y f(x2) = %0.6f' % (step, x2, f(x2)))

        if f(x0, fx) * f(x2, fx) < 0:
            x1 = x2
        else:
            x0 = x2

        step = step + 1
        condicion = abs(f(x2, fx)) > e

    print('\nRaiz: %0.8f' % x2)

x0 = float(input('x0: '))
x1 = float(input('x1: '))
e = float(input('Toleracia: '))
fx = input('Funcion: ')


if f(x0, fx) * f(x1, fx) > 0.0:
    print('Intenta otros valores')
else:
    falsePosition(x0,x1,e,fx)
