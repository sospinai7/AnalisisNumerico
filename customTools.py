from sympy import var
from sympy import sympify
from sympy import log, exp

def imprimir(datos, resultados):
    print(*datos, sep='   ')
    for res in resultados:
        print(*res, sep='   ')
        
def f(incog, x, funcion):
    user_input = funcion # 'x**3-5*x-9'
    expr = sympify(user_input)
    resultado = expr.subs(incog, x)
    return resultado