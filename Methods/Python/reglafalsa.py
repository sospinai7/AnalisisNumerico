#!/home/salzatec1/miniconda3/bin/python

import math

def reglafalsa(func, a, b, Nmax, tol):
    if a > b:
        print("'A' cannot be greater than 'B'")
        return

    if a*b > 0:
        print("Interval ends must have opposite signs.")

    fa = func(a)
    fb = func(b)
    if fb-fa == 0:
        print("Error: Division by zero")
        return

    pm = (fb*a-fa*b)/(fb-fa)
    fpm = func(pm)
    
    E = 1000
    count = 1
    print("|{i:^3}|{a:^20}|{xm:^20}|{b:^20}|{fxm:^20}|{E:^10}|".format(i="i",a="a",xm="xm",b="b",fxm="f(xm)",E="E"))
    while (count < Nmax) and (E > tol):
        text = "|{i:3g}| {a:.16f} | {xm:.16f} | {b:.16f} | {fpm:.16f} | {E:.1E} |"
        print(text.format(i=count, a=a, xm=pm, b=b, fpm=fpm, E=E))
        if (fa * fpm) < 0:
            b = pm
            fb = fpm
        else:
            a = pm
            fa = fpm
        
        p0 = pm
        if fb-fa == 0:
            print("Error: Division by zero")
            return
        pm = (fb*a - fa*b)/(fb-fa)
        fpm = func(pm)
        E = abs(pm-p0)
        count += 1

    if count == Nmax or E > tol:
        print("The method is not converging")

def funcion(x):
    #return math.exp(x) + math.sin(x)
    return 1.0000*(x**3) - 6.8000*(x**2) + 13.1600*x - 7.8400
    #return math.log(math.sin(x)**2 + 1) - 1/2

def main():
    reglafalsa(funcion, 1, 1.9, 100, 1e-7)

if __name__ == '__main__':
    main()
