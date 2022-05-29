from sympy import var
import customTools as ct


def bisection(f, t_error, a, b, tol, maxiter):
    """
    :param f: funcion
    :param a: The x-axis value where f(a)<0
    :param b: The x-axis value where f(b)>0
    :param tol: tolerancia
    :param maxiter: maximo numero de iteraciones
    :return: The x-axis value of the root,
                number of iterations used
    """
    x = var('x')
    fa = ct.f(x, a, f)
    fb = ct.f(x, b, f)
    if fa == 0:
        print(a, ' es una raíz')
    elif fb == 0:
        print(b, ' es una raíz')
    elif fa*fb < 0:
        result = []
        mid = (a+b)*0.5  # Declare mid as the midpoint ab
        fmid = ct.f(x, mid, f)
        error = tol + 1
        result.append([0,a,fa,b,fb,mid,fmid,error]) # Storing data for 0 iteration
        n = 1  # Start with 1 iteration
        while fmid != 0 and error > tol and n <= maxiter:
            if fa*fmid < 0:
                b = mid
                fb = fmid
            else:
                a = mid
                fa = fmid
            last  = mid
            mid = (a+b)*0.5 
            fmid = ct.f(x, mid, f)
            
            if t_error == 1:
                error = abs(mid-last)
            else:
                error = abs((mid-last)/mid)
            result.append([n,a,fa,b,fb,mid,fmid,error])
            n += 1
        
        ct.imprimir(['Iteration', 'xini', 'f(xini)',
        'xsup', 'f(xsup)', 'xmid', 'f(xmid)', 'Error'], result)

        if fmid == 0:
            print(mid, ' is a root')
        elif error <= tol:
            print(mid, ' is close to a root with a tolerance of ', tol)
        else:
            print('Iteration limit exceded')
    else:
        print('Wrong range')


'''y = lambda x: x**3 + 2*x**2 - 5
root, iterations = bisection(y, -5, 5, 0.00001, 100)
print ("Raiz:", root)
print ("Iteracion: ", iterations)'''




