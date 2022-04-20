import numpy as np
from sympy import var
import customTools as ct


def incremental_search(exp, x0, delta, imax):
    """
    :param f --> exp: The function to solve
    :param x0: Initial value for x
    :param a: The left boundary x-axis value(to discuss)
    :param b: The right boundary x-axis value(to discuss)
    :param dx --> delta: The incremental value in searching
    :param imax: max limit of iterations
    :return: The x-axis value of the root,
                number of iterations used
    """
    #fa = f(a) 
    #c = a + dx 
    #fc = f(c)    
    #n = 1
    
    x = var('x')
    fx0 = ct.f(x, x0, exp)
    if fx0 == 0:
        print(x0, 'Es una raíz')
    else:
        result = []
        result.append([0,x0,fx0])
        x1 = x0 + delta
        fx1 = ct.f(x, x1, exp)
        i = 1
        result.append([i,x1,fx1])

        #np.sign(fa) == np.sign(fc) equal to fx0*fx1 > 0
        while fx0*fx1 > 0 and i <= imax:
            x0 = x1
            fx0 = fx1
            x1 = x0 + delta
            fx1 = ct.f(x, x1, exp)
            i += 1
            result.append([i,x1,fx1])
            
            #if a >= b:
                #return a - dx, n
            """ a = c
            fa = fc
            c = a + dx
            fc = f(c)
            n += 1 """
        ct.imprimir(['Iteration', 'x', 'f(x)'], result)
        if fx1 == 0:
            print(x1, ' is a root')
        elif fx0*fx1 < 0:
            print('There is a root between ', x0, ' and ', x1)
            #return c, n
        else:
            # return (a + c)/2., n
            print('Iteration limit exceded')

y = lambda x: x**3 + 2.0*x**2 - 5

root, iterations = incremental_search(y, -5., 5., 0.001)

print("Root is:", root)
print("Iterations:", iterations)

