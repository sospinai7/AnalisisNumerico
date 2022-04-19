#!/usr/bin/env python
# coding: utf-8
from sympy import var
from sympy import sympify

# Defining Function3
def f(x, funcion):
    incognita = var('x')
    # user_input = 'x**3-5*x-9'
    user_input = funcion
    expr = sympify(user_input)
    res = expr.subs(incognita, x)
    return res

# Implementing False Position Method
def falsePosition(x0,x1,e,fx):
    step = 1

    condition = True
    while condition:
        x2 = x0 - (x1-x0) * f(x0, fx)/( f(x1, fx) - f(x0, fx) )
        #print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))

        if f(x0, fx) * f(x2, fx) < 0:
            x1 = x2
        else:
            x0 = x2

        step = step + 1
        condition = abs(f(x2, fx)) > e

    print('\nRaiz: %0.8f' % x2)

x0 = float(input('x0: '))
x1 = float(input('x1: '))
e = float(input('Toleracia: '))
fx = input('Funcion: ')


# Checking Correctness of initial guess values and false positioning
if f(x0, fx) * f(x1, fx) > 0.0:
    print('Given guess values do not bracket the root.')
    print('Try Again with different guess values.')
else:
    falsePosition(x0,x1,e,fx)

# # Defining Function
# def f(fx, x):
#     incognita = var('x')  # the possible variable names must be known beforehand...
#     user_input = fx
#     expr = sympify(user_input)
#     res = expr.subs(incognita, x)
#     print(res)  # -1.322..
#     return res
#     #return x**3-5*x-9

# def falsePosition(x0,x1,e):
#     step = 1


#     condition = True
#     while condition:
#         x2 = x0 - (x1-x0) * f(x0)/( f(x1) - f(x0) )
#         #print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))

#         if f(x0) * f(x2) < 0:
#             x1 = x2
#         else:
#             x0 = x2

#         step = step + 1
#         condition = abs(f(x2)) > e

#     print('\nRequired root is: %0.8f' % x2)

# fx = input('Function: ')
# x0 = float(input('First Guess: '))
# x1 = float(input('Second Guess: '))
# e = float(input('Tolerable Error: '))


# # Checking Correctness of initial guess values and false positioning
# if f(fx, x0) * f(fx, x1) > 0.0:
#     print('Given guess values do not bracket the root.')
#     print('Try Again with different guess values.')
# else:
#     falsePosition(x0,x1,e)
