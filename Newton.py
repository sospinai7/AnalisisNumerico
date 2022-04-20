from sympy import var
import customTools as ct

def newton(f, df, t_error, x, tol, maxiter):
    """
    :param f: The function to solve
    :param df: The derivative function of f
    :param x: Initial guess value of x
    :param tol: The precision of the solution
    :param maxiter: Maximum number of iterations
    :param t_error: type of error to work with
    :return: The x-axis value of the root,
                number of iterations used
    """
    sig = var('x') # char 'x' inside the expresion
    n = 1
    result = []
    fx = ct.f(sig, x, f)
    dx = ct.f(sig, x, df)
    error = tol + 1
    result.append([n,x,fx,dx,error])
    
    while fx != 0 and error > tol and n <= maxiter:
        x1 = x - fx/dx
        fx = ct.f(sig, x1, f)
        dx = ct.f(sig, x1, df)
        if t_error == 1:
            error = abs(x1 - x)
        else:
            error = abs((x1 - x)/x1)
        #if abs(x1 - x) < tol:  # Root is very close
        #    return x1, n
        x = x1
        n += 1
        result.append([n,x,fx,dx,error])
    
    ct.imprimir(['Iteration', 'x', 'f(x)', 'df(x)', 'Error'], result)
    if fx == 0:
        print(x, ' is a root')
    elif error <= tol:
        print(x, 'is close to a root with a tolerance of ', tol)
    else:
        print('Iteration limit exceded')

    #return None, n 

'''y = lambda x: x**3 + 2*x**2 - 5
dy = lambda x: 3*x**2 + 4*x
root, iterations = newton(y, dy, 5.0, 0.00001, 100)
print("La Raiz es: ", root)
print("Iteracions: ", iterations)'''
