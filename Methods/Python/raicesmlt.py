#!/home/salzatec1/miniconda3/bin/python

from sympy import *
import math

def raicesmlt(f, df, d2f, x0, Nmax, tol):
    xant = x0;
    fant = f(xant)
    dfant = df(xant)
    E = 1000
    i = 0
    print("|{i:^3}|{xi:^16}|{fxm:^20}|{E:^10}|".format(i="i",xi="xi",fxm="f(xi)",E="E"))
    while i < Nmax and E > tol:
        print("|{i:3g}|{xi:.16f}|{fxm:.16f}|{E:.1E}|".format(i=0, xi=xant, fxm=fant, E=E))
        if ((df(xant)**2 - fant*d2f(xant))) == 0:
            print("Error: division by zero")
            return

        xact = xant - fant*df(xant)/((df(xant)**2 - fant*d2f(xant)))
        fact = f(xact)
        E = abs(xact-xant)
        xant = xact
        fant = fact
        i += 1

    if i == Nmax or E > tol:
        print("El metodo no converge con los datos dados")
    else:
        #print("X{i} = {xi:.16f} | f(x{i}) = {fant:.16f}| Error = {E:.1E}".format(i=i, xi=xant, fant=fant, E=E))
        print("El metodo converge a x:", xact, "en la iteracion", i)

def main():
    x = Symbol('x')
    func = fun(x)
    f = lambdify(x, func)
    #dfStr = func.diff(x)
    #df = lambdify(x, dfStr)
    #d2fStr = dfStr.diff(x)
    #d2f = lambdify(x, d2fStr)
    df = lambdify(x, exp(x)-1)
    d2f = lambdify(x, exp(x))

    raicesmlt(f, df, d2f, 1, 100, 1e-7)

def fun(x):
    #return math.exp(x) + math.sin(x)
    return exp(x) - x - 1

if __name__=='__main__':
    main()
