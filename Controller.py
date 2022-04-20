from traceback import print_list
from unittest import result
#from sympy import var
#from sympy import sympify
from FixedPoint import fixed_point
from IncrementalSearch import incremental_search

"""
x = var('x')
expr = input()
func = sympify(expr)
initx = input()
res = func.subs(x, initx)
print(res)
"""
#from methods.busquedas import busquedasIn
     
def opciones():
    opc = [
        'Incremental searches (1)',
        'Bisection (2)',
        'Fixed Point (4)',
    ]
    print(*opc, sep='\n')
    print('#: ', end="")
    num = input()
    if num == '1':
        print('f(x): ', end="")
        exp = input()
        print('x0: ', end="")
        x0 = float(input())
        print('increase of x: ', end="")
        delta = float(input())
        print('max limit of iterations: ', end="")
        imax = int(input())
        incremental_search(exp, x0, delta, imax)
        
        
    elif num == '4':
        print('f(x): ', end="")
        exp = input()
        print('g(x): ', end="")
        g_exp = input()
        print('x0: ', end="")
        x0 = float(input())
        print('type of error (1)abs (2)rel: ', end="")
        t_error = int(input())
        print('max limit of iterations: ', end="")
        imax = int(input())
        print('tolerance: ', end="")
        tol = float(input())
        fixed_point(exp, g_exp, x0, t_error, imax, tol)

def main():
    print('**** Type the method you want to use ****')
    opciones()
        
if __name__ == "__main__":
    main()