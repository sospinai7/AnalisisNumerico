#!/bin/python3

import math

def busqueda(func, xin, delta, Nmax):
    if delta<=0:
        print('Delta value can not be negative')
        return

    xant = xin
    fant = func(xant)
    xact = xant + delta
    fact = func(xact)
    
    i = 1
    print(" {i:^3}| {a:^20}|{b:^20}".format(i="i",a="xant",b="xact"))
    for i in range(1, Nmax):
        text = '{:3g} | {:.16f} | {:.16f}'
        print(text.format(i, xant, xact))
        if (fant * fact) < 0:
            break
        else:
            xant = xact
            fant = fact
            xact = xant + delta
            fact = func(xact)

    a = xant
    b = xact


def funcion(x):
    #return math.exp(x) + math.sin(x)
    return math.log(math.sin(x)**2 + 1) - 1/2

def main():
    busqueda(funcion, -3, 0.5, 100)
    #print(2.55+0.05)

if __name__ == '__main__':
    main()
