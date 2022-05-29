#!/home/salzatec1/miniconda3/bin/python

from sympy import *
import math

def secante(f, x0, x1, Nmax, tol):

    f0 = f(x0)
    f1 = f(x1)
    E = 1000
    print("X{i} = {x0:.16f} | f(x{i}) = {f0:.16f} |".format(i=0, x0=x0, f0=f0))
    print("X{i} = {x0:.16f} | f(x{i}) = {f0:.16f} |".format(i=1, x0=x1, f0=f1))
    i = 2

    while i < Nmax and E > tol:
        if f1-f0 == 0:
            print("Error: Division by zero")
            return
        xact = x1 -f1*((x1-x0)/(f1-f0))
        fact = f(xact)
        E = abs(xact-x1)
        print("X{i} = {xact:.16f} | f(x{i}) = {fact:.16f} | E{i} = {E:.1E} |".format(i=i, xact=xact, fact=fact, E=E))
        #print("X{i} =".format(i=i), xact,"|","f(x{i}) =".format(i=i), fact,"|","Error =", E)
        x0 = x1
        f0 = f1
        x1 = xact
        f1 = fact
        i += 1

    if i == Nmax or E > tol:
        print("El metodo no converge con los datos dados")
    else:
        print("El metodo converge a x:", xact, "en la iteracion", i-1)

def main():
    x = Symbol('x')
    secante(funcion(x), 0.5, 1, 100, 1e-7)

def funcion(x):
    #return math.exp(x) + math.sin(x)
    return ln(sin(x)**2 +1) - 1/2

if __name__=='__main__':
    main()
