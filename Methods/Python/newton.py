#!/home/salzatec1/miniconda3/bin/python

from sympy import *
import math

def newton(f, df, x0, Nmax, tol):
    xant = x0;
    fant = f(xant)
    dfant = df(xant)
    E = 1000
    i = 0

    print("|{i:^3}|{xi:^20}|{fxi:^20}|{E:^10}|".format(i="i",xi="xm",fxi="f(xi)",E="E"))
    while i < Nmax and E > tol:
        print("|{i:3g}| {xi:.16f} | {fxi:.16f} | {E:.1E} |".format(i=i, xi=xant, fxi=fant, E=E))
        #print("X{i} =".format(i=i), xant,"|","f(x{i}) =".format(i=i), fant,"|","Error =", E)
        if  fant-dfant == 0:
            print("Error: division by zero")
            return

        xact = xant - (fant/dfant)
        fact = f(xact)
        dfact = df(xact)
        E = abs(xact-xant)
        xant = xact
        fant = fact
        dfant = dfact
        i += 1

    if i == Nmax or E > tol:
        print("El metodo no converge con los datos dados")
    else:
        #print("|{i:3g}| {xi:.16f} | {fxi:.16f} | {E:.1E} |".format(i=i, xi=xant, fxi=fant, E=E))
        #print("X{i} =".format(i=i), xact,"|","f(x{i}) =".format(i=i), fact,"|","Error =", E)
        print("El metodo converge a x:", xact, "en la iteracion:", i)

    return xact


def main():
    x = Symbol('x')
    func = fun(x)
    f = lambdify(x, func)
    df = lambdify(x, dfun(x))
    #df = lambdify(x, func.diff(x))

    newton(f, df, 0.5, 100, 1e-7)

def fun(x):
    #return math.exp(x) + math.sin(x)
    return ln(sin(x)**2 + 1) - 1/2

def dfun(x):
    return 2*((sin(x)**2 + 1)**-1)*sin(x)*cos(x)

if __name__=='__main__':
    main()
